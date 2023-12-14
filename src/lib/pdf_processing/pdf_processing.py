from typing import List, Optional
import pdfplumber
from utils.logger import logger

def parse_large_pdf(pdf_path: str):
    pages: List[str] = []

    pdf: Optional[pdfplumber.pdf.PDF] = None
    try:
        pdf = pdfplumber.open(pdf_path)
        for page in pdf.pages:
            text: str = page.extract_text()
            pages.append(text)
    except FileNotFoundError:
        logger.error(f"Error: File not found - {pdf_path}")
    except Exception as e:
        logger.error(f"Error: {e}")
    finally:
        close_pdf(pdf)

    return pages

def close_pdf(pdf: Optional[pdfplumber.pdf.PDF]):
    if pdf:
        pdf.close()
        logger.info("PDF file closed.")
