# TaxInvoiceExtractor

This repository presents my solution to the assignment on Extracting and Analyzing Tax Invoices.

Here is a brief overview and additional details on how I handled certain aspects of the code:

1. **Code Structure:**
   I utilized reusable functions and modules (utils and pdf extractor) following a service-oriented architecture. To accommodate another invoice type, you can create another service inheriting from the abstract Invoice class.

2. **Data Extraction:**
   I adopted a scalable approach by streaming and processing one page at a time. The data insertion is performed using 'insert all' functionality.

3. **Data Storage:**
   PostgreSQL is employed for data storage, with ORM used for interacting with the database.

4. **Deduplication:**
   A unique index has been created on the combined Xref and Total Loan Amount to prevent duplicates. Additionally, I used `on_conflict_do_nothing` so that only new entries are inserted when a combination of new and duplicate entries is encountered.

5. **SQL Operations:**
   Please review the functions `total_loan_amount_in_given_date_range` and `highest_loan_by_broker` in `src/service/tax_invoice/tax_invoice.py`.

6. **Reporting:**
   Check out the functions `generate_broker_report`, `total_loan_amount_by_date`, `tier_level_by_transaction`, and `loans_by_tier_and_date` in `src/service/tax_invoice/tax_invoice.py`.

### Dependencies

```
Python 3.11.6
pip 23.3.1
```

### Installation

Create a virtual environment:
```
python -m venv venv
```

Activate it::
```
source venv/bin/activate
```

Install Dependencies:
```
pip install -r requirements.txt
```

Create a .env file outside the src directory and fill it with the following information:
```
PDF_PATH="/path/to/TaxInvoiceExtractor/src/TestPDF.pdf"
POSTGRES_DB=pdf_extractor
POSTGRES_USER=root
POSTGRES_PASSWORD=123
POSTGRES_HOST=localhost
POSTGRES_PORT=5433

```

Make the scripts executable (Optional):
```
chmod +x src/script/start_postgresql.sh
chmod +x src/script/stop_postgresql.sh
```

If PostgreSQL is not installed, use the script to run a Docker container of PostgreSQL (Optional):
```
./src/script/start_postgresql.sh
```

Stop the container:
```
./src/script/stop_postgresql.sh
```

### Usage

Set up the table in PostgreSQL:
```
python setup.py
```

Run the script:
```
python main.py
```
