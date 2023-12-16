from typing import Optional, Dict, List, Union
import camelot
from datetime import datetime

from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import IntegrityError

from services.invoice import Invoice
from services.tax_invoice.model.tax_invoice import TaxInvoiceModel

from utils.logger import logger
from utils.dbpool import engine, metadata

TaxInvoiceType = Dict[str, Union[int, str, float]]


class TaxInvoice(Invoice):
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path

    def get_app_id_and_xref(self, inp: str) -> (str, str):
        return tuple(inp.split())

    def get_brorrower_sub_broker(self, inp: str) -> (str, str):
        inp_len: int = len(inp)
        split_point: int = inp_len
        for i in range(inp_len - 1, 0, -1):
            if inp[i] == "\n" or inp[i].islower():
                split_point = i
                break

        if split_point == inp_len:
            return (inp.strip(), None)
        else:
            sub_broker: str = inp[: split_point + 1]
            borrower_name: str = inp[split_point + 1 :]
            return (borrower_name.strip(), sub_broker.strip())

    def process_data(self, tables: Optional[camelot.core.TableList]):
        all_data: List[TaxInvoiceType] = []
        for table in tables:
            for index, row in table.df.iterrows():
                if index != 0 and index != 1:
                    if len(row) != 10:
                        logger.error(
                            "The row is not in correct format. Row no: %d", index - 1
                        )
                    app_id, xref = self.get_app_id_and_xref(row[0])
                    borrower_name, sub_broker = self.get_brorrower_sub_broker(row[3])
                    data: TaxInvoiceType = {
                        "app_id": int(app_id.strip()),
                        "xref": int(xref.strip()),
                        "settlement_date": datetime.strptime(
                            row[1].strip(), "%d/%m/%Y"
                        ).date(),
                        "broker": row[2].strip(),
                        "sub_broker": sub_broker,
                        "borrower_name": borrower_name,
                        "description": row[4].strip(),
                        "total_loan_amount": float(row[5].strip().replace(",", "")),
                        "comm_rate": float(row[6].strip().replace(",", "")),
                        "upfront": float(row[7].strip().replace(",", "")),
                        "upfront_incl_gst": float(row[9].strip().replace(",", "")),
                    }
                    all_data.append(data)
        # print(all_data)
        self.insert_data(all_data)

    def insert_data(self, data: List[TaxInvoiceType]):
        TaxInvoiceModel.metadata = metadata
        try:
            with Session(engine) as session:
                # session.bulk_insert_mappings(TaxInvoiceModel, data, render_nulls=True)
                stmt = (
                    insert(TaxInvoiceModel.__table__)
                    .values(data)
                    .on_conflict_do_nothing()
                )

                # Execute the statement
                session.execute(stmt)

                # Commit the transaction
                session.commit()
                logger.info("Data inserted successfully.")
        except IntegrityError as e:
            # Log the error using the logger
            logger.error("Error inserting data into tax_invoice table: %s", e.orig)
        except Exception as e:
            # Log other unexpected errors
            logger.error("Unexpected error: %s", e)
