import React from 'react';
import { Wallet, Plus, Calendar, Download } from 'lucide-react';

const MONTH_NAMES = [
  "Januari", "Februari", "Maret", "April", "Mei", "Juni",
  "Juli", "Agustus", "September", "Oktober", "November", "Desember"
];

export default function Header({ 
  selectedMonth, 
  selectedYear, 
  onMonthChange, 
  onYearChange, 
  onOpenAddModal,
  onExportCSV
}) {
  const currentYear = new Date().getFullYear();
  const years = Array.from({ length: 5 }, (_, i) => currentYear - 2 + i);

  return (
    <header className="header">
      <div className="brand">
        <div className="brand-icon">
          <Wallet size={26} />
        </div>
        <div className="brand-title">
          <h1>Catatan Pengeluaran</h1>
          <p>Kelola & Analisis Keuangan Rumah Tangga</p>
        </div>
      </div>

      <div className="header-controls">
        <div className="month-selector">
          <Calendar size={18} style={{ color: '#94a3b8' }} />
          <select 
            value={selectedMonth} 
            onChange={(e) => onMonthChange(Number(e.target.value))}
          >
            {MONTH_NAMES.map((name, idx) => (
              <option key={idx + 1} value={idx + 1}>
                {name}
              </option>
            ))}
          </select>

          <select 
            value={selectedYear} 
            onChange={(e) => onYearChange(Number(e.target.value))}
          >
            {years.map((yr) => (
              <option key={yr} value={yr}>
                {yr}
              </option>
            ))}
          </select>
        </div>

        <button className="btn-secondary" onClick={onExportCSV} title="Download Laporan CSV">
          <Download size={18} />
          <span>Export CSV</span>
        </button>

        <button className="btn-primary" onClick={onOpenAddModal}>
          <Plus size={18} />
          <span>Tambah Pengeluaran</span>
        </button>
      </div>
    </header>
  );
}
