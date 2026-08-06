from fastapi import FastAPI, Depends, HTTPException, Query, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import extract, func, or_
from typing import List, Optional
from datetime import datetime, date, timedelta
import calendar

import models, schemas, database

# Inisialisasi Database Tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="Household Expense Tracker API",
    description="Backend API untuk Pencatatan Pengeluaran Bulanan Rumah Tangga",
    version="1.0.0"
)

# CORS Configuration agar React Frontend dapat berkomunikasi dengan API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Pada produksi disesuaikan dengan URL Frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Master Data Kategori & Tipe Pengeluaran
MASTER_CATEGORIES = [
    "Makanan & Bahan Pokok",
    "Tagihan & Utilitas",
    "Transportasi & Bensin",
    "Hiburan & Jajan",
    "Top Up & E-Wallet",
    "Kesehatan & Obat",
    "Pendidikan & Anak",
    "Perlengkapan Rumah",
    "Lain-lain"
]

MASTER_TYPES = [
    "Belanja",
    "Tagihan",
    "Jajan",
    "Ongkos",
    "Topup",
    "Lainnya"
]

# Seed Data Awal jika database masih kosong (Sangat berguna untuk Demo Free)
def seed_dummy_data_if_empty(db: Session):
    if db.query(models.Expense).count() == 0:
        today = date.today()
        dummy_items = [
            models.Expense(
                title="Belanja Mingguan Supermarket",
                amount=650000,
                category="Makanan & Bahan Pokok",
                expense_type="Belanja",
                date=today - timedelta(days=1),
                notes="Sayur, daging, buah, dan beras"
            ),
            models.Expense(
                title="Bayar Tagihan Listrik PLN",
                amount=280000,
                category="Tagihan & Utilitas",
                expense_type="Tagihan",
                date=today.replace(day=2) if today.day >= 2 else today,
                notes="Listrik token 200rb + admin"
            ),
            models.Expense(
                title="Beli Bensin Mobil & Motor",
                amount=150000,
                category="Transportasi & Bensin",
                expense_type="Ongkos",
                date=today - timedelta(days=3),
                notes="Pertalite full tank"
            ),
            models.Expense(
                title="Topup ShopeePay & GoPay",
                amount=200000,
                category="Top Up & E-Wallet",
                expense_type="Topup",
                date=today - timedelta(days=4),
                notes="Untuk persiapan pesanan online"
            ),
            models.Expense(
                title="Jajan Kopi & Boba",
                amount=45000,
                category="Hiburan & Jajan",
                expense_type="Jajan",
                date=today - timedelta(days=2),
                notes="Kopi susu gula aren"
            ),
            models.Expense(
                title="Tagihan Internet Wi-Fi Rumah",
                amount=350000,
                category="Tagihan & Utilitas",
                expense_type="Tagihan",
                date=today.replace(day=5) if today.day >= 5 else today,
                notes="IndiHome 30Mbps"
            ),
            models.Expense(
                title="Belanja Sabun & Deterjen",
                amount=120000,
                category="Perlengkapan Rumah",
                expense_type="Belanja",
                date=today - timedelta(days=5),
                notes="Pembersih lantai & deterjen"
            )
        ]
        db.add_all(dummy_items)
        db.commit()

# Run seed on startup
@app.on_event("startup")
def startup_db_seed():
    db = database.SessionLocal()
    try:
        seed_dummy_data_if_empty(db)
    finally:
        db.close()

# Root API Info
@app.get("/")
def read_root():
    return {
        "status": "online",
        "message": "Household Expense Tracker API Python FastAPI is running",
        "docs": "/docs"
    }

# Master Data Endpoints
@app.get("/api/master-data")
def get_master_data():
    return {
        "categories": MASTER_CATEGORIES,
        "types": MASTER_TYPES
    }

# GET All Expenses with Filter (Month, Year, Category, Type, Search)
@app.get("/api/expenses", response_model=List[schemas.ExpenseResponse])
def get_expenses(
    month: Optional[int] = Query(None, ge=1, le=12),
    year: Optional[int] = Query(None, ge=2000, le=2100),
    category: Optional[str] = None,
    expense_type: Optional[str] = None,
    search: Optional[str] = None,
    db: Session = Depends(database.get_db)
):
    query = db.query(models.Expense)

    if year:
        query = query.filter(extract('year', models.Expense.date) == year)
    if month:
        query = query.filter(extract('month', models.Expense.date) == month)
    if category:
        query = query.filter(models.Expense.category == category)
    if expense_type:
        query = query.filter(models.Expense.expense_type == expense_type)
    if search:
        search_pattern = f"%{search}%"
        query = query.filter(
            or_(
                models.Expense.title.ilike(search_pattern),
                models.Expense.notes.ilike(search_pattern)
            )
        )

    return query.order_by(models.Expense.date.desc(), models.Expense.id.desc()).all()

# POST New Expense
@app.post("/api/expenses", response_model=schemas.ExpenseResponse, status_code=status.HTTP_201_CREATED)
def create_expense(
    expense: schemas.ExpenseCreate,
    db: Session = Depends(database.get_db)
):
    db_expense = models.Expense(**expense.model_dump())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

# GET Single Expense
@app.get("/api/expenses/{expense_id}", response_model=schemas.ExpenseResponse)
def get_expense(expense_id: int, db: Session = Depends(database.get_db)):
    expense = db.query(models.Expense).filter(models.Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Pengeluaran tidak ditemukan")
    return expense

# PUT Update Expense
@app.put("/api/expenses/{expense_id}", response_model=schemas.ExpenseResponse)
def update_expense(
    expense_id: int,
    updated_data: schemas.ExpenseUpdate,
    db: Session = Depends(database.get_db)
):
    db_expense = db.query(models.Expense).filter(models.Expense.id == expense_id).first()
    if not db_expense:
        raise HTTPException(status_code=404, detail="Pengeluaran tidak ditemukan")

    update_dict = updated_data.model_dump(exclude_unset=True)
    for key, value in update_dict.items():
        setattr(db_expense, key, value)

    db.commit()
    db.refresh(db_expense)
    return db_expense

# DELETE Expense
@app.delete("/api/expenses/{expense_id}", status_code=status.HTTP_200_OK)
def delete_expense(expense_id: int, db: Session = Depends(database.get_db)):
    db_expense = db.query(models.Expense).filter(models.Expense.id == expense_id).first()
    if not db_expense:
        raise HTTPException(status_code=404, detail="Pengeluaran tidak ditemukan")

    db.delete(db_expense)
    db.commit()
    return {"message": "Pengeluaran berhasil dihapus", "id": expense_id}

# GET Summary Analytics Response
@app.get("/api/summary", response_model=schemas.SummaryResponse)
def get_summary(
    month: Optional[int] = Query(None, ge=1, le=12),
    year: Optional[int] = Query(None, ge=2000, le=2100),
    db: Session = Depends(database.get_db)
):
    now = date.today()
    target_month = month if month else now.month
    target_year = year if year else now.year

    # Query items for target month & year
    query = db.query(models.Expense).filter(
        extract('year', models.Expense.date) == target_year,
        extract('month', models.Expense.date) == target_month
    )
    items = query.all()

    total_amount = sum(item.amount for item in items)
    total_count = len(items)

    # Days in month calculation
    _, num_days = calendar.monthrange(target_year, target_month)
    # If current month, calculate up to today's day for average
    days_elapsed = now.day if (now.year == target_year and now.month == target_month) else num_days
    days_elapsed = max(1, days_elapsed)
    average_daily = total_amount / days_elapsed

    # Summary by category
    category_map = {}
    for item in items:
        category_map[item.category] = category_map.get(item.category, 0) + item.amount

    by_category = []
    for cat_name in MASTER_CATEGORIES:
        cat_total = category_map.get(cat_name, 0)
        if cat_total > 0:
            percentage = (cat_total / total_amount * 100) if total_amount > 0 else 0
            count = sum(1 for item in items if item.category == cat_name)
            by_category.append({
                "category": cat_name,
                "total": cat_total,
                "percentage": round(percentage, 1),
                "count": count
            })

    # Sort categories by total descending
    by_category.sort(key=lambda x: x["total"], reverse=True)

    # Summary by type
    type_map = {}
    for item in items:
        type_map[item.expense_type] = type_map.get(item.expense_type, 0) + item.amount

    by_type = []
    for type_name in MASTER_TYPES:
        type_total = type_map.get(type_name, 0)
        if type_total > 0:
            percentage = (type_total / total_amount * 100) if total_amount > 0 else 0
            count = sum(1 for item in items if item.expense_type == type_name)
            by_type.append({
                "expense_type": type_name,
                "total": type_total,
                "percentage": round(percentage, 1),
                "count": count
            })

    by_type.sort(key=lambda x: x["total"], reverse=True)

    # Default monthly budget benchmark for households (dapat disesuaikan)
    monthly_budget = 5000000.0

    return {
        "total_amount": total_amount,
        "total_count": total_count,
        "average_daily": round(average_daily, 0),
        "monthly_budget": monthly_budget,
        "by_category": by_category,
        "by_type": by_type
    }
