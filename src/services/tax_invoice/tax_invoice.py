import camelot
from services.invoice import Invoice
from utils.logger import logger
from typing import Optional


class TaxInvoice(Invoice):
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path

    def process_data(self, tables: Optional[camelot.core.TableList]):
        for table in tables:
            for _, row in table.df.iterrows():
                print(row)
        return
