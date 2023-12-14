import pdfplumber

def parse_large_pdf(pdf_path):
    pages = []

    try:
        pdf = pdfplumber.open(pdf_path)
        for page in pdf.pages:
            text = page.extract_text()
            pages.append(text)
    except FileNotFoundError:
        print(f"Error: File not found - {pdf_path}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        close_pdf(pdf)

    return pages

def close_pdf(pdf):
    if pdf:
        pdf.close()
        print("PDF file closed.")
