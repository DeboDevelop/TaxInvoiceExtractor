# TaxInvoiceExtractor

This is my answer to the assignment of Extracting and Analysing Tax Invoice.

Here is a brief and extra bits on how I handled certain aspect of the code:
1. Code structure:
I have used reusable functions and moduels (utils and pdf extractor) and service oriented architecture. If we have to add another invoice, we have create another service and have it inherit the Invoice abstract class.

2. Data Extraction
I am streaming and processing one page to make it scalable. I used insert all to insert the data.

3. Data Storage
I used Posgresql for data storage and used ORM for it.

4. Deduplication
I created a unique index on combined Xref and Total Loan Amount to disallow duplicates. I also used `on_conflict_do_nothing` so if we have combination of new and duplicate entries, only new entries are inserted.

5. SQL Operations
Please check `total_loan_amount_in_given_date_range` and `highest_loan_by_broker` in `src/service/tax_invoice/tax_invoice.py`.

6. Reporting
Please check `generate_broker_report`, `total_loan_amount_by_date`, `tier_level_by_transaction` and `loans_by_tier_and_date` in `src/service/tax_invoice/tax_invoice.py`.


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

Adtivate it:
```
source venv/bin/activate
```

Install Dependencies:
```
pip install -r requirements.txt
```

Create a .env file out side src and fill it with following information:
```
PDF_PATH="/path/to/TaxInvoiceExtractor/src/TestPDF.pdf"
POSTGRES_DB=pdf_extractor
POSTGRES_USER=root
POSTGRES_PASSWORD=123
POSTGRES_HOST=localhost
POSTGRES_PORT=5433

```

Make the script executatable (Optional):
```
chmod +x src/script/start_postgresql.sh
chmod +x src/script/stop_postgresql.sh
```

If you don't ahve posgresql installed, use to script to run a docker container of posgresql (Optional):
```
./src/script/start_postgresql.sh
```

Stop the container:
```
./src/script/stop_postgresql.sh
```

Usage

Setup the Table in Postgresql:
```
python setup.py
```

Run the script:
```
python main.py
```
