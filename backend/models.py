from sqlalchemy import Column, Integer, String, Float, Date, DateTime
from datetime import datetime
from database import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String(50), nullable=False, index=True)
    expense_type = Column(String(50), nullable=False, index=True) # e.g. Belanja, Tagihan, Jajan, Ongkos, Topup
    date = Column(Date, nullable=False, index=True)
    notes = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
