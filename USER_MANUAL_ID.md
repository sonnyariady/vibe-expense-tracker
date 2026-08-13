# 📖 Panduan Pengguna (User Manual)
## Aplikasi Pencatatan Pengeluaran Rumah Tangga (Household Expense Tracker)

**Versi Aplikasi:** 1.0.0  
**Bahasa:** Bahasa Indonesia  
**Tanggal:** Agustus 2026  

---

## 📋 Daftar Isi
1. [Pendahuluan & Fitur Utama](#1-pendahuluan--fitur-utama)
2. [Navigasi Header & Mode Penyimpanan](#2-navigasi-header--mode-penyimpanan)
3. [Membaca Dashboard & KPI Summary Cards](#3-membaca-dashboard--kpi-summary-cards)
4. [Visualisasi Analisis Grafik](#4-visualisasi-analisis-grafik)
5. [Menambah Catatan Pengeluaran Baru](#5-menambah-catatan-pengeluaran-baru)
6. [Pencarian Real-Time & Filter Transaksi](#6-pencarian-real-time--filter-transaksi)
7. [Mengubah & Menghapus Transaksi](#7-mengubah--menghapus-transaksi)
8. [Mengekspor Laporan ke CSV](#8-mengekspor-laporan-ke-csv)
9. [Troubleshooting & Tanya Jawab (FAQ)](#9-troubleshooting--tanya-jawab-faq)

---

## 1. Pendahuluan & Fitur Utama

**Aplikasi Pencatatan Pengeluaran Rumah Tangga** adalah aplikasi web modern yang dirancang khusus untuk mempermudah Anda dalam mencatat, mengelompokkan, menganalisis pengeluaran bulanan keluarga, serta memantau sisa anggaran (budget).

### ✨ Fitur Unggulan:
* **Dual-Mode Storage**: Berjalan secara persisten dengan database backend Python FastAPI + SQLite, atau otomatis beralih ke *LocalStorage Browser* saat offline/demo mode.
* **Manajemen Anggaran (Budget Target)**: Monitoring persentase penggunaan anggaran bulanan dengan indikator warna (*Hijau*, *Kuning*, *Merah Alert*).
* **Visualisasi Data Interaktif**: Grafik Donut untuk distribusi Kategori dan Grafik Batang untuk Tipe Pengeluaran.
* **Filter & Pencarian Instan**: Cari transaksi berdasarkan kata kunci, filter kategori, atau tipe pengeluaran.
* **Ekspor CSV**: Unduh laporan pengeluaran bulanan dalam format file CSV yang siap dibuka di Microsoft Excel atau Google Sheets.

---

## 2. Navigasi Header & Mode Penyimpanan

Pada bagian paling atas halaman, terdapat bar navigasi utama aplikasi:

![Header & Navigasi Periode](docs/screenshots/01_header_period_navigation.png)

### Elemen-elemen Header:
1. **Judul & Logo**: Menampilkan nama aplikasi "💸 Household Expense Tracker".
2. **Selector Bulan & Tahun**: Gunakan dropdown **Bulan** dan **Tahun** untuk memilih periode laporan pengeluaran yang ingin Anda lihat atau catat.
3. **Indikator Mode Storage**:
   * 🟢 **FastAPI Server (SQLite)**: Terhubung ke database server lokal. Data tersimpan permanen.
   * 🟡 **Demo Mode (LocalStorage)**: Backend tidak aktif, data disimpan di browser.
4. **Tombol Export CSV**: Mengunduh seluruh transaksi periode aktif ke file CSV.
5. **Tombol + Tambah Pengeluaran**: Membuka dialog formulir untuk menambah transaksi baru.

---

## 3. Membaca Dashboard & KPI Summary Cards

Dashboard menyediakan 4 kartu statistik utama (KPI Cards) untuk memberikan gambaran cepat finansial Anda pada bulan berjalan:

![Dashboard & KPI Cards](docs/screenshots/02_kpi_dashboard.png)

### Detail Kartu Statistik:
1. **Total Pengeluaran Bulan Ini**:
   * Menampilkan total akumulasi pengeluaran dalam Rupiah (Rp) untuk bulan & tahun yang dipilih.
2. **Batas Anggaran Bulanan & Sisa**:
   * Menampilkan batas anggaran bulanan (Default: Rp 5.000.000) dan sisa saldo anggaran yang belum terpakai.
   * Progress Bar Warna:
     * 🟢 **Hijau (< 75%)**: Pengeluaran masih aman.
     * 🟡 **Kuning (75% - 100%)**: Pengeluaran mendekati batas anggaran.
     * 🔴 **Merah (> 100%)**: Pengeluaran telah melebihi batas anggaran bulanan.
3. **Estimasi Rata-rata Harian**:
   * Rata-rata estimasi biaya yang dikeluarkan per hari pada bulan ini.
4. **Total Transaksi**:
   * Jumlah transaksi yang telah tercatat pada periode ini.

---

## 4. Visualisasi Analisis Grafik

Aplikasi ini dilengkapi dengan dua jenis grafik interaktif untuk membantu Anda menganalisis ke mana saja uang Anda dialokasikan:

![Visualisasi Grafik Analisis](docs/screenshots/03_visual_analytics.png)

1. **Grafik Donut (Persentase Kategori)**:
   * Memvisualisasikan persentase pengeluaran berdasarkan Kategori (contoh: *Makanan & Bahan Pokok*, *Tagihan & Utilitas*, *Transportasi*, *Pendidikan*, dll.).
   * Arahkan kursor (*hover*) pada bagian donut untuk melihat detail nominal dan persentase tepatnya.
2. **Grafik Batang (Tipe Pengeluaran)**:
   * Membandingkan total nominal pengeluaran berdasarkan Tipe (*Belanja*, *Tagihan*, *Jajan*, *Ongkos*, *Topup*, *Lainnya*).

---

## 5. Menambah Catatan Pengeluaran Baru

Untuk mencatat pengeluaran baru, ikuti langkah-langkah berikut:

![Modal Tambah Pengeluaran](docs/screenshots/04_add_expense_modal.png)

### Langkah-langkah:
1. Klik tombol **`+ Tambah Pengeluaran`** di pojok kanan atas header.
2. Jendela formulir modal akan muncul. Isi kolom berikut:
   * **Nama Transaksi** *(Wajib)*: Masukkan nama pengeluaran (contoh: `Belanja Sembako Mingguan`).
   * **Nominal (Rp)** *(Wajib)*: Masukkan angka saja tanpa titik atau koma (contoh: `350000`).
   * **Tanggal** *(Wajib)*: Pilih tanggal transaksi dilakukan.
   * **Kategori** *(Wajib)*: Pilih salah satu dari dropdown (*Makanan*, *Tagihan*, *Transportasi*, dll.).
   * **Tipe Pengeluaran** *(Wajib)*: Pilih tipe pengeluaran (*Belanja*, *Tagihan*, *Jajan*, *Ongkos*, *Topup*, *Lainnya*).
   * **Catatan** *(Opsional)*: Tambahkan keterangan rinci jika diperlukan.
3. Klik tombol hijau **`Simpan Transaksi`**.
4. Data baru akan langsung muncul pada tabel dan memperbarui grafik serta statistik KPI secara real-time.

---

## 6. Pencarian Real-Time & Filter Transaksi

Jika Anda memiliki puluhan catatan transaksi, gunakan fitur Filter dan Pencarian pintar di atas tabel transaksi:

![Filter dan Pencarian](docs/screenshots/05_filters_and_search.png)

* **Kolom Pencarian Kata Kunci**: Ketik nama transaksi atau catatan (contoh: `Beras` atau `Listrik`) untuk mencari secara instan.
* **Dropdown Filter Kategori**: Filter tabel agar hanya menampilkan transaksi dari kategori tertentu (contoh: *Makanan & Bahan Pokok*).
* **Dropdown Filter Tipe**: Filter tabel berdasarkan tipe pengeluaran tertentu (contoh: *Tagihan*).

---

## 7. Mengubah & Menghapus Transaksi

Anda dapat memperbarui atau menghapus data transaksi yang sudah dicatat kapan saja melalui kolom **Aksi** pada tabel transaksi:

![Aksi Edit dan Hapus](docs/screenshots/06_action_edit_delete.png)

* **Mengubah Data Transaksi (Edit)**:
  1. Klik ikon **Pensil (Edit)** pada baris transaksi yang ingin diubah.
  2. Modal edit akan terbuka dengan data transaksi saat ini.
  3. Lakukan perubahan data yang diinginkan, lalu klik **`Simpan Perubahan`**.
* **Menghapus Transaksi (Delete)**:
  1. Klik ikon **Tong Sampah (Hapus)** pada baris transaksi yang ingin dihapus.
  2. Dialog konfirmasi akan muncul. Klik **`Hapus`** untuk mengonfirmasi.

---

## 8. Mengekspor Laporan ke CSV

Aplikasi memfasilitasi pembuatan laporan finansial fisik/digital dalam format `.CSV`:

![Ekspor CSV](docs/screenshots/07_export_csv.png)

### Cara Ekspor:
1. Pastikan Anda telah memilih periode **Bulan** dan **Tahun** yang sesuai.
2. Klik tombol **`Export CSV`** di bagian kanan header.
3. File laporan bernama `Laporan_Pengeluaran_M_YYYY.csv` (contoh: `Laporan_Pengeluaran_8_2026.csv`) akan otomatis terunduh ke folder Downloads di komputer Anda.
4. Anda dapat membuka file ini menggunakan **Microsoft Excel**, **Google Sheets**, atau aplikasi spreadsheet lainnya.

---

## 9. Troubleshooting & Tanya Jawab (FAQ)

> [!TIP]
> **Pertanyaan Umum & Solusi:**
>
> 1. **Bagaimana jika indikator menampilkan "Demo Mode (LocalStorage)"?**  
>    *Ini artinya server FastAPI backend tidak terdeteksi. Aplikasi tetap berfungsi normal dan menyimpan data Anda di penyimpanan browser lokal.*
>
> 2. **Apakah data saya aman saat dalam Demo Mode?**  
>    *Ya, data disimpan secara aman dalam browser Anda. Namun jika Anda menghapus cache/history browser, data demo dapat terhapus. Sebaiknya gunakan backend FastAPI untuk penyimpanan persisten jangka panjang.*
>
> 3. **Bagaimana cara mengubah batas anggaran bulanan (Budget Limit)?**  
>    *Batas anggaran default diset sebesar Rp 5.000.000. Pengaturannya dapat disesuaikan pada file konfigurasi aplikasi.*
