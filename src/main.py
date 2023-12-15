import os
from dotenv import load_dotenv
from pdf_processing.pdf_processing import parse_large_pdf
from services.tax_invoice.tax_invoice import TaxInvoice

if __name__ == "__main__":
    load_dotenv()
    PDF_PATH = os.environ.get("PDF_PATH")
    tax_invoice = TaxInvoice(PDF_PATH)
    parse_large_pdf(tax_invoice)
