# 💸 Aplikasi Pencatatan Pengeluaran Rumah Tangga (Household Expense Tracker)

Aplikasi Web Modern untuk mencatat, mengelompokkan, dan menganalisis pengeluaran bulanan rumah tangga secara mendalam. Dibangun menggunakan **Python FastAPI** di sisi Backend dan **ReactJS (Vite)** di sisi Frontend, lengkap dengan visualisasi grafik interaktif dan fitur ekspor laporan.

---

## ✨ Fitur Utama
1. **Pencatatan Transaksi Lengkap**:
   - Tanggal Pengeluaran
   - Nama Transaksi & Catatan
   - Nominal (Format IDR Rupiah)
   - Kategori (Makanan & Bahan Pokok, Tagihan, Transportasi, Hiburan, Top Up, Kesehatan, dll)
   - Tipe Pengeluaran (**Belanja**, **Tagihan**, **Jajan**, **Ongkos**, **Topup**, **Lainnya**)
2. **Dashboard Analytics & KPI Cards**:
   - Total Pengeluaran Bulan Ini
   - Batas Anggaran Bulanan & Sisa Anggaran (Progress Bar)
   - Estimasi Rata-rata Pengeluaran Harian
   - Jumlah Transaksi
3. **Visualisasi Data (Recharts)**:
   - **Donut Chart**: Distribusi Pengeluaran berdasarkan Kategori.
   - **Bar Chart**: Distribusi Pengeluaran berdasarkan Tipe (Belanja vs Tagihan vs Jajan vs Ongkos vs Topup).
4. **Filter & Pencarian**:
   - Filter Bulan & Tahun
   - Filter Kategori & Tipe Pengeluaran
   - Real-time Search Keyword
5. **Ekspor Data**: Download data laporan transaksi dalam format `.CSV` / Excel.
6. **Dual Mode Storage**: Terhubung ke FastAPI + SQLite Database, serta fallback ke **LocalStorage Browser** jika dijalankan tanpa backend server (cocok untuk Demo Statis Free).

---

## 🛠 Tech Stack
- **Backend**: Python 3.10+ | FastAPI | SQLite | SQLAlchemy | Pydantic v2 | Uvicorn
- **Frontend**: React 18 | Vite | Recharts | Lucide React | Modern Custom CSS Glassmorphism

---

## 🚀 Cara Menjalankan Aplikasi Secara Lokal

### 1. Menjalankan Backend (Python FastAPI)

Buka terminal di folder root project `PengeluaranBulanan`:

```bash
# Enter folder backend
cd backend

# Aktifkan Virtual Environment (Windows)
.\venv\Scripts\activate

# Install dependensi (jika belum)
pip install -r requirements.txt

# Jalankan server FastAPI
uvicorn main:app --reload --port 8000
```

Server backend akan berjalan di: **`http://127.0.0.1:8000`**  
Dokumentasi OpenAPI / Swagger UI otomatis dapat diakses di: **`http://127.0.0.1:8000/docs`**

---

### 2. Menjalankan Frontend (ReactJS Vite)

Buka terminal kedua di folder root project `PengeluaranBulanan`:

```bash
# Enter folder frontend
cd frontend

# Install dependensi npm
npm install

# Jalankan server dev React
npm run dev
```

Frontend akan berjalan di: **`http://localhost:3000`** (atau URL yang ditampilkan di terminal). Buka browser dan aplikasi siap digunakan!

---

## 💡 Ide & Cara Simpan Data untuk Demo Free & Publikasi (Deploy Gratis)

Berikut beberapa strategi untuk mempublikasikan aplikasi ini ke internet secara **100% GRATIS**:

### 🔹 Opsi 1: SQLite + Render.com + Vercel (Paling Direkomendasikan)
1. **Backend (Render.com)**:
   - Buat akun gratis di [Render.com](https://render.com).
   - Buat **New Web Service**, hubungkan repository Git berisi folder `backend`.
   - Set Build Command: `pip install -r requirements.txt`
   - Set Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Data SQLite otomatis tersimpan di file `pengeluaran.db`.
2. **Frontend (Vercel)**:
   - Buat akun gratis di [Vercel.com](https://vercel.com).
   - Import repository Git berisi folder `frontend`.
   - Vercel akan otomatis mendeteksi Vite React dan melakukan build secara instan.

---

### 🔹 Opsi 2: Supabase / Neon (Cloud PostgreSQL Free Tier)
Jika ingin data tersimpan di Cloud Database yang lebih tangguh:
1. Buat database PostgreSQL gratis di **[Supabase.com](https://supabase.com)** atau **[Neon.tech](https://neon.tech)**.
2. Di file `backend/database.py`, ganti `SQLALCHEMY_DATABASE_URL` dengan Connection String dari Supabase (misal: `postgresql://user:password@ep-xyz.neon.tech/dbname`).
3. Push backend ke Render / Railway / Koyeb (Free Tier).

---

### 🔹 Opsi 3: Demo Offline / Static Mode (Tanpa Backend Server)
- Aplikasi frontend React yang dibuat sudah dilengkapi dengan **Automatic Fallback Mode**.
- Jika Backend FastAPI tidak menyala atau di-deploy secara terpisah di **GitHub Pages / Vercel**, aplikasi akan beralih secara otomatis menggunakan **LocalStorage Browser**.
- Calon user/penguji demo dapat mencoba tambah, edit, hapus, filter, dan melihat grafik pengeluaran 100% langsung dari browser tanpa perlu menyalakan server backend!

---

## 📁 Struktur Direktori Project
```text
PengeluaranBulanan/
├── backend/
│   ├── database.py       # Konfigurasi SQLite & SQLAlchemy session
│   ├── main.py           # Endpoint REST API FastAPI & seed data
│   ├── models.py         # Schema tabel database Expense
│   ├── schemas.py        # Pydantic data validation schemas
│   ├── requirements.txt  # Package dependensi Python
│   └── pengeluaran.db    # Database SQLite lokal (dibuat otomatis)
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/   # Header, StatCard, ExpenseCharts, ExpenseTable, ExpenseFormModal
│   │   ├── api.js        # Service layer API & LocalStorage Fallback
│   │   ├── App.jsx       # Main App Component
│   │   ├── index.css     # Design system & Styling UI
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
└── README.md
```
