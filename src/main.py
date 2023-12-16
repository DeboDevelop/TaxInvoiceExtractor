import os
from dotenv import load_dotenv
from pdf_processing.pdf_processing import parse_large_pdf
from services.tax_invoice.tax_invoice import TaxInvoice

if __name__ == "__main__":
    load_dotenv()
    PDF_PATH = os.environ.get("PDF_PATH")
    tax_invoice = TaxInvoice(PDF_PATH)
    parse_large_pdf(tax_invoice)
    result_total_loan = tax_invoice.total_loan_amount_in_given_date_range(
        "17/10/2023", "25/10/2023"
    )
    result_highest_loan = tax_invoice.highest_loan_by_broker("Steve Dahu")
    print("Calculate the total loan amount during a specific time period.")
    print(result_total_loan)
    print()

    print("Calculate the highest loan amount given by a broker.")
    print(result_highest_loan)
    print()

    print(
        "Generate a report for the broker, sorting loan amounts in descending order from \
    maximum to minimum, covering daily periods."
    )
    daily_report = tax_invoice.generate_broker_report("Stratton Norwest", "daily")
    for dr in daily_report:
        print(dr)
    print()

    print(
        "Generate a report for the broker, sorting loan amounts in descending order from \
    maximum to minimum, covering weekly periods."
    )
    weekly_report = tax_invoice.generate_broker_report("Stratton Norwest", "weekly")
    for wr in weekly_report:
        print(wr)
    print()

    print(
        "Generate a report for the broker, sorting loan amounts in descending order from \
    maximum to minimum, covering monthly periods."
    )
    monthly_report = tax_invoice.generate_broker_report("Stratton Norwest", "monthly")
    for mr in monthly_report:
        print(mr)
    print()

    print("Generate a report of the total loan amount grouped by date.")
    total_loan_amt = tax_invoice.total_loan_amount_by_date()
    for tl in total_loan_amt:
        print(tl)

    print("Define tier level of each transaction")
    tier_level_trs = tax_invoice.tier_level_by_transaction()
    for t in tier_level_trs:
        print(t)
    print()

    print("Generate a report of the number of loans under each tier group by date.")
    loan_tier = tax_invoice.loans_by_tier_and_date()
    for lt in loan_tier:
        print(lt)
    print()
