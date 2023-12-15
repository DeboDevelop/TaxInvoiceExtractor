from typing import Optional, Type
import camelot
import fitz
from utils.logger import logger
from services.invoice import Invoice


def get_page_numbers(pdf_path):
    pdf_document: Optional[fitz.Document] = None
    total_pages: int = 0
    try:
        pdf_document = fitz.open(pdf_path)
        total_pages = pdf_document.page_count
    except Exception as e:
        logger.error("Error:  %s", e, exc_info=True)
    finally:
        if pdf_document:
            pdf_document.close()
    return total_pages


def parse_large_pdf(invoice: Type[Invoice]):
    total_pages: int = get_page_numbers(invoice.pdf_path)
    tables: Optional[camelot.core.TableList] = None
    try:
        for i in range(1, total_pages + 1):
            tables = camelot.read_pdf(invoice.pdf_path, flavor="stream", pages=str(i))
            invoice.process_data(tables)
    except FileNotFoundError:
        logger.error("Error: File not found - %s", invoice.pdf_path)
    except Exception as e:
        logger.error("Error:  %s", e, exc_info=True)
