# 💸 Household Expense Tracker (Aplikasi Pencatatan Pengeluaran Rumah Tangga)

[![GitHub Repository](https://img.shields.io/badge/GitHub-sonnyariady%2Fvibe--expense--tracker-blue?logo=github)](https://github.com/sonnyariady/vibe-expense-tracker)
[![Backend](https://img.shields.io/badge/Backend-Python%20FastAPI%20%7C%20SQLite-009688?logo=fastapi)](file:///c:/Latihan/Fullstack/PengeluaranBulanan/backend)
[![Frontend](https://img.shields.io/badge/Frontend-React%20%7C%20Vite-61DAFB?logo=react)](file:///c:/Latihan/Fullstack/PengeluaranBulanan/frontend)

A modern full-stack web application designed for tracking, categorizing, analyzing monthly household expenses, and setting budget targets. Features interactive charts, real-time filtering, CSV exporting, and dual data storage mode (FastAPI + SQLite with offline LocalStorage fallback).

---

## 🌐 Table of Contents / Daftar Isi
- [🇮🇩 Bahasa Indonesia](#-bahasa-indonesia)
  - [Fitur Utama](#-fitur-utama)
  - [📖 User Manual / Petunjuk Penggunaan](#-user-manual--petunjuk-penggunaan)
  - [🛠 Tech Stack & Arsitektur](#-tech-stack--arsitektur)
  - [🚀 Cara Menjalankan Aplikasi (Lokal)](#-cara-menjalankan-aplikasi-lokal)
  - [🌐 Opsi Deployment Gratis](#-opsi-deployment-gratis)
- [🇬🇧 English Version](#-english-version)
  - [Key Features](#-key-features)
  - [📖 User Manual](#-user-manual)
  - [🛠 Tech Stack & Architecture](#-tech-stack--architecture)
  - [🚀 Quick Start Guide (Local)](#-quick-start-guide-local)
  - [🌐 Free Deployment Options](#-free-deployment-options)
- [📁 Directory Structure](#-directory-structure)

---

# 🇮🇩 Bahasa Indonesia

## ✨ Fitur Utama
1. **Pencatatan Transaksi Lengkap**:
   - Tanggal pengeluaran, nama transaksi, nominal (format IDR Rupiah).
   - **Kategori**: Makanan & Bahan Pokok, Tagihan & Utilitas, Transportasi, Hiburan, Top Up, Kesehatan, Perlengkapan, Pendidikan, dll.
   - **Tipe Pengeluaran**: Belanja, Tagihan, Jajan, Ongkos, Topup, Lainnya.
   - Catatan tambahan opsional.
2. **Dashboard Analytics & KPI Cards**:
   - **Total Pengeluaran Bulan Ini** dalam Rupiah.
   - **Batas Anggaran Bulanan & Sisa Anggaran**: dilengkapi dengan progress bar warna otomatis (*Green*, *Yellow*, *Red Alert* jika melebihi budget).
   - **Estimasi Rata-rata Harian**: menghitung pengeluaran rata-rata per hari.
   - **Total Transaksi**: statistik jumlah transaksi yang tercatat.
3. **Visualisasi Data Interaktif (Recharts)**:
   - **Donut Chart**: Distribusi persentase pengeluaran berdasarkan Kategori.
   - **Bar Chart**: Perbandingan pengeluaran berdasarkan Tipe (Belanja vs Tagihan vs Jajan vs Ongkos vs Topup).
4. **Filter & Pencarian Pintar**:
   - Selector Bulan & Tahun.
   - Filter Kategori & Tipe Pengeluaran.
   - Pencarian *Real-time Keyword*.
5. **Ekspor Data**: Fitur unduh laporan transaksi dalam format `.CSV` yang kompatibel dengan Microsoft Excel / Google Sheets.
6. **Dual-Mode Storage**:
   - **FastAPI + SQLite**: Penyimpanan database lokal persisten.
   - **LocalStorage Fallback**: Otomatis beralih ke penyimpanan browser jika backend tidak aktif (cocok untuk Demo Statis).

---

## 📖 User Manual / Petunjuk Penggunaan

> 📄 **Download User Manual PDF & Documentation:**
> - 🇮🇩 **Bahasa Indonesia:** [USER_MANUAL_ID.pdf](USER_MANUAL_ID.pdf) (File PDF Lengkap) | [USER_MANUAL_ID.md](USER_MANUAL_ID.md) (Dokumen Markdown)
> - 🇬🇧 **English Version:** [USER_MANUAL_EN.pdf](USER_MANUAL_EN.pdf) (Full PDF File) | [USER_MANUAL_EN.md](USER_MANUAL_EN.md) (Markdown Document)
> - 📸 **Screenshots Directory:** [docs/screenshots/](docs/screenshots)

### 1. Navigasi Header & Periode
* **Pilih Bulan & Tahun**: Gunakan dropdown bulan dan tahun di baris atas header untuk berpindah periode laporan bulanan.
* **Status Mode**: Indikator di bawah header menampilkan apakah aplikasi terhubung ke **Python FastAPI Server (SQLite)** atau berjalan di **Demo Mode (LocalStorage Browser)**.

### 2. Membaca Dashboard & KPI Cards
* **Total Pengeluaran**: Menampilkan total uang yang telah dikeluarkan pada bulan & tahun yang dipilih.
* **Batas Anggaran (Budget)**: 
  * Menampilkan alokasi anggaran bulanan (default Rp 5.000.000).
  * Indikator warna: **Hijau** (penggunaan aman < 75%), **Kuning** (peringatan 75% - 100%), **Merah** (melebihi batas anggaran > 100%).
* **Rata-rata Harian**: Menunjukkan estimasi pengeluaran per hari pada bulan berjalan.
* **Jumlah Transaksi**: Menampilkan kuantitas transaksi yang sudah dicatat.

### 3. Menambah Catatan Pengeluaran Baru
1. Klik tombol hijau **`+ Tambah Pengeluaran`** di kanan atas.
2. Isi formulir modal:
   * **Nama Transaksi** (contoh: *Beli Beras & Minyak Goreng*).
   * **Nominal (Rp)** (contoh: *150000*).
   * **Tanggal** (default: hari ini).
   * **Kategori** (pilih kategori yang paling sesuai).
   * **Tipe Pengeluaran** (pilih *Belanja*, *Tagihan*, *Jajan*, *Ongkos*, *Topup*, atau *Lainnya*).
   * **Catatan** *(Opsional)*.
3. Klik tombol **`Simpan Transaksi`**. Data akan langsung diperbarui di tabel & grafik.

### 4. Mengubah & Menghapus Transaksi
* **Mengedit Transaksi**: Pada tabel daftar transaksi, klik ikon **Edit (Pensil)** di kolom Aksi pada baris transaksi yang ingin diubah. Ubah data lalu klik **`Simpan Perubahan`**.
* **Menghapus Transaksi**: Klik ikon **Hapus (Tong Sampah)** di kolom Aksi. Konfirmasi penghapusan saat dialog muncul.

### 5. Menggunakan Filter & Pencarian
* **Pencarian Kata Kunci**: Ketik nama transaksi atau catatan di kolom pencarian *"Cari transaksi..."*.
* **Filter Kategori**: Filter transaksi berdasarkan kategori spesifik (contoh: *Makanan & Bahan Pokok*).
* **Filter Tipe**: Filter transaksi berdasarkan tipe pengeluaran (contoh: *Jajan* atau *Tagihan*).

### 6. Mengekspor Laporan ke CSV (Excel)
1. Pilih periode Bulan dan Tahun yang ingin diekspor.
2. Klik tombol **`Export CSV`** di bagian header.
3. File `.csv` (contoh: `Laporan_Pengeluaran_8_2026.csv`) akan otomatis diunduh ke komputer Anda.

---

## 🛠 Tech Stack & Arsitektur

### Backend
* **Python 3.10+**
* **FastAPI**: Framework REST API performa tinggi.
* **SQLite**: Database terintegrasi (*file-based*).
* **SQLAlchemy**: Object-Relational Mapping (ORM).
* **Pydantic v2**: Validasi data input & output schema.

### Frontend
* **React 18 & Vite**: Fast HMR & build modern toolchain.
* **Recharts**: Responsive chart visualization library.
* **Lucide React**: Vector icons UI set.
* **Custom CSS Glassmorphism**: Modern dark/light glass design system.

---

## 🚀 Cara Menjalankan Aplikasi (Lokal)

### Prerequisites
* **Python 3.10+** terinstall
* **Node.js 18+** & **npm** terinstall

### Langkah 1: Menjalankan Backend (FastAPI)
```bash
# Pindah ke directory backend
cd backend

# Aktifkan Virtual Environment (Windows)
.\venv\Scripts\activate

# Install dependencies Python
pip install -r requirements.txt

# Menjalankan server FastAPI
uvicorn main:app --reload --port 8000
```
Backend berjalan di: **`http://127.0.0.1:8000`**  
Dokumentasi Interactive API (Swagger UI): **`http://127.0.0.1:8000/docs`**

---

### Langkah 2: Menjalankan Frontend (React Vite)
Buka terminal baru di root folder:
```bash
# Pindah ke directory frontend
cd frontend

# Install dependencies node_modules
npm install

# Menjalankan React Dev Server
npm run dev
```
Frontend berjalan di: **`http://localhost:3000`**

---

## 🌐 Opsi Deployment Gratis

1. **Backend (Render.com)**: Deploy folder `backend` sebagai **Web Service** gratis di Render.
2. **Frontend (Vercel / Netlify)**: Deploy folder `frontend` secara gratis di Vercel atau Netlify.
3. **Demo Mode (GitHub Pages)**: Karena dilengkapi dengan *LocalStorage Fallback*, frontend bisa langsung dideploy statis di GitHub Pages tanpa backend server active!

---

<br/>

---

# 🇬🇧 English Version

## ✨ Key Features
1. **Comprehensive Expense Tracking**:
   - Transaction date, title, amount in IDR currency.
   - **Categories**: Groceries & Food, Utilities & Bills, Transportation, Entertainment, Top Up, Healthcare, Supplies, Education, etc.
   - **Expense Types**: Shopping, Bills, Snacks, Transit, Top Up, Others.
   - Optional detailed notes.
2. **Analytics Dashboard & KPI Cards**:
   - **Total Monthly Expense** in Rupiah.
   - **Monthly Budget & Remaining Limit**: Progress bar with dynamic color indicators (*Green*, *Yellow*, *Red Alert* when exceeding budget).
   - **Daily Expense Average**: Calculated daily spending rate for the current month.
   - **Total Transactions**: Total headcount of recorded items.
3. **Interactive Data Visualization (Recharts)**:
   - **Donut Chart**: Category expense distribution.
   - **Bar Chart**: Breakdown by Expense Types (Shopping vs Bills vs Snacks vs Transit vs Topup).
4. **Smart Search & Filter**:
   - Month & Year picker.
   - Category & Type filter dropdowns.
   - Real-time keyword search.
5. **Data Export**: Export monthly transactions report directly into `.CSV` format (compatible with MS Excel / Google Sheets).
6. **Dual Storage Architecture**:
   - **FastAPI + SQLite**: Persistent local backend storage.
   - **LocalStorage Fallback**: Automatic failover to client-side storage when backend server is offline.

---

## 📖 User Manual

### 1. Header Navigation & Period Selection
* **Select Month & Year**: Use the Month and Year dropdown selectors in the top header bar to switch between reporting periods.
* **Storage Status Banner**: Displays whether the app is currently connected to **Python FastAPI (SQLite)** or running in **Demo Mode (LocalStorage Browser)**.

### 2. Dashboard KPIs & Budget Tracker
* **Total Expenses**: Displays the total accumulated spending for the selected period.
* **Monthly Budget Target**:
  * Default budget set to Rp 5,000,000.
  * Color indicators: **Green** (< 75% budget used), **Yellow** (75% - 100%), **Red** (> 100% budget overspent).
* **Daily Average**: Estimated average spending per day for the selected month.
* **Total Count**: Number of logged transactions.

### 3. Adding a New Expense Entry
1. Click the green **`+ Tambah Pengeluaran`** button in the top right.
2. Fill out the entry modal form:
   * **Title** (e.g., *Monthly Groceries & Milk*).
   * **Amount (Rp)** (e.g., *150000*).
   * **Date** (defaults to today's date).
   * **Category** (select from standard category list).
   * **Expense Type** (*Belanja / Tagihan / Jajan / Ongkos / Topup / Lainnya*).
   * **Notes** *(Optional)*.
3. Click **`Simpan Transaksi`**. The dashboard, charts, and table update instantaneously.

### 4. Editing & Deleting Expenses
* **Edit Expense**: In the transaction list table, click the **Pencil icon** on the row you wish to modify. Make your changes and click **`Simpan Perubahan`**.
* **Delete Expense**: Click the **Trash Can icon** on the transaction row and confirm deletion in the popup dialog.

### 5. Filtering & Search
* **Search Input**: Type any keyword in the search bar to filter transactions by title or notes.
* **Category Filter**: Filter transactions by specific category.
* **Type Filter**: Filter transactions by spending type.

### 6. Exporting Reports to CSV
1. Select the desired Month and Year.
2. Click **`Export CSV`** in the header.
3. A formatted `.csv` file (e.g., `Laporan_Pengeluaran_8_2026.csv`) will automatically download to your computer.

---

## 🛠 Tech Stack & Architecture

### Backend
* **Python 3.10+**
* **FastAPI**
* **SQLite Database**
* **SQLAlchemy ORM**
* **Pydantic v2**

### Frontend
* **React 18 & Vite**
* **Recharts Visualization Library**
* **Lucide React UI Icons**
* **Custom CSS Glassmorphism Design System**

---

## 🚀 Quick Start Guide (Local)

### Prerequisites
* **Python 3.10+**
* **Node.js 18+** & **npm**

### Step 1: Run Backend (FastAPI)
```bash
cd backend
.\venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```
Backend API will run at: **`http://127.0.0.1:8000`**  
OpenAPI / Swagger documentation: **`http://127.0.0.1:8000/docs`**

---

### Step 2: Run Frontend (React Vite)
In a separate terminal:
```bash
cd frontend
npm install
npm run dev
```
Frontend Web App will run at: **`http://localhost:3000`**

---

## 🌐 Free Deployment Options

1. **Backend**: Host the `backend` folder on [Render.com](https://render.com) (Free Web Service).
2. **Frontend**: Host the `frontend` folder on [Vercel](https://vercel.com) or [Netlify](https://netlify.com).
3. **Static Demo**: Host on [GitHub Pages](https://pages.github.com) using the client-side LocalStorage mode.

---

## 📁 Directory Structure

```text
PengeluaranBulanan/
├── backend/
│   ├── database.py       # SQLite connection & SQLAlchemy session
│   ├── main.py           # FastAPI REST endpoints & seed data
│   ├── models.py         # Expense database table model
│   ├── schemas.py        # Pydantic validation schemas
│   ├── requirements.txt  # Python packages
│   └── pengeluaran.db    # SQLite local DB file
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/   # Header, StatCard, ExpenseCharts, ExpenseTable, ExpenseFormModal
│   │   ├── api.js        # API service layer with LocalStorage fallback
│   │   ├── App.jsx       # Main App component
│   │   ├── index.css     # Glassmorphism styling system
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
└── README.md             # Project documentation & user manual
```

---
*Developed with ❤️ using Python FastAPI & ReactJS (Vite).*
