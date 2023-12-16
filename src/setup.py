from utils.dbpool import engine
from utils.logger import logger

from services.tax_invoice.model.tax_invoice import TaxInvoice


def setup():
    TaxInvoice.metadata.create_all(bind=engine, checkfirst=True)
    logger.info("Table created successfully.")


if __name__ == "__main__":
    setup()
