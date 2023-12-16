from sqlalchemy import Column, Integer, Date, String, Float, Index
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TaxInvoice(Base):
    __tablename__ = 'tax_invoice'
    app_id = Column(Integer, primary_key=True)
    xref = Column(Integer)
    settlement_date = Column(Date)
    broker = Column(String(255))
    sub_broker = Column(String(255))
    borrower_name = Column(String(255))
    description = Column(String(255))
    total_loan_amount = Column(Float)
    comm_rate = Column(Float)
    upfront = Column(Float)
    upfront_incl_gst = Column(Float)

