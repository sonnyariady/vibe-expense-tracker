from pydantic import BaseModel, Field
from datetime import date as date_type, datetime
from typing import Optional, List, Dict

class ExpenseBase(BaseModel):
    title: str = Field(..., example="Bayar Listrik PLN")
    amount: float = Field(..., gt=0, example=250000)
    category: str = Field(..., example="Tagihan & Utilitas")
    expense_type: str = Field(..., example="Tagihan") # Belanja, Tagihan, Jajan, Ongkos, Topup
    date: date_type = Field(..., example="2026-08-01")
    notes: Optional[str] = Field(None, example="Pembayaran via M-Banking")

class ExpenseCreate(ExpenseBase):
    pass

class ExpenseUpdate(BaseModel):
    title: Optional[str] = None
    amount: Optional[float] = None
    category: Optional[str] = None
    expense_type: Optional[str] = None
    date: Optional[date_type] = None
    notes: Optional[str] = None

class ExpenseResponse(ExpenseBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class CategorySummary(BaseModel):
    category: str
    total: float
    percentage: float
    count: int

class TypeSummary(BaseModel):
    expense_type: str
    total: float
    percentage: float
    count: int

class SummaryResponse(BaseModel):
    total_amount: float
    total_count: int
    average_daily: float
    monthly_budget: float
    by_category: List[CategorySummary]
    by_type: List[TypeSummary]
