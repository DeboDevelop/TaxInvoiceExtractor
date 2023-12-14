import pdfplumber

def parse_large_pdf(pdf_path):
    pages = []

    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                pages.append(text)
    except FileNotFoundError:
        print(f"Error: File not found - {pdf_path}")
    except Exception as e:
        print(f"Error: {e}")

    return pages
