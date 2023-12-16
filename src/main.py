import os
from dotenv import load_dotenv
from pdf_processing.pdf_processing import parse_large_pdf
from services.tax_invoice.tax_invoice import TaxInvoice

if __name__ == "__main__":
    load_dotenv()
    PDF_PATH = os.environ.get("PDF_PATH")
    tax_invoice = TaxInvoice(PDF_PATH)
    # parse_large_pdf(tax_invoice)
    result_total_loan = tax_invoice.total_loan_amount_in_given_date_range(
        "17/10/2023", "25/10/2023"
    )
    result_highest_loan = tax_invoice.highest_loan_by_broker(
        "Steve Dahu"
    )
    print(result_total_loan)
    print(result_highest_loan)
    daily_report = tax_invoice.generate_broker_report("Stratton Norwest", "daily")
    for dr in daily_report:
        print(dr)
    weekly_report = tax_invoice.generate_broker_report("Stratton Norwest", "weekly")
    for wr in weekly_report:
        print(wr)
    monthly_report = tax_invoice.generate_broker_report("Stratton Norwest", "monthly")
    for mr in monthly_report:
        print(mr)
    print()
