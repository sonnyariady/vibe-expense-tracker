import React, { useState, useEffect, useCallback } from 'react';
import Header from './components/Header';
import StatCard, { formatRupiah } from './components/StatCard';
import ExpenseCharts from './components/ExpenseCharts';
import ExpenseTable from './components/ExpenseTable';
import ExpenseFormModal from './components/ExpenseFormModal';
import { 
  fetchExpenses, 
  fetchSummary, 
  createExpense, 
  updateExpense, 
  deleteExpense 
} from './api';
import { Info, Database } from 'lucide-react';

export default function App() {
  const currentDate = new Date();
  const [selectedMonth, setSelectedMonth] = useState(currentDate.getMonth() + 1);
  const [selectedYear, setSelectedYear] = useState(currentDate.getFullYear());
  
  const [expenses, setExpenses] = useState([]);
  const [summary, setSummary] = useState(null);
  
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('');
  const [selectedType, setSelectedType] = useState('');

  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingExpense, setEditingExpense] = useState(null);
  const [isFallbackMode, setIsFallbackMode] = useState(false);

  // Load Data from Backend API (or LocalStorage Fallback)
  const loadData = useCallback(async () => {
    try {
      const [expRes, sumRes] = await Promise.all([
        fetchExpenses({
          month: selectedMonth,
          year: selectedYear,
          category: selectedCategory,
          expense_type: selectedType,
          search: searchQuery
        }),
        fetchSummary({
          month: selectedMonth,
          year: selectedYear
        })
      ]);

      setExpenses(expRes.data);
      setSummary(sumRes.data);
      setIsFallbackMode(expRes.isFallback);
    } catch (error) {
      console.error('Error loading expenses:', error);
    }
  }, [selectedMonth, selectedYear, selectedCategory, selectedType, searchQuery]);

  useEffect(() => {
    loadData();
  }, [loadData]);

  // Add / Edit Submit Handler
  const handleFormSubmit = async (formData) => {
    try {
      if (editingExpense) {
        await updateExpense(editingExpense.id, formData);
      } else {
        await createExpense(formData);
      }
      setIsModalOpen(false);
      setEditingExpense(null);
      loadData();
    } catch (err) {
      alert('Gagal menyimpan pengeluaran: ' + err.message);
    }
  };

  // Delete Handler
  const handleDelete = async (id) => {
    if (window.confirm('Apakah Anda yakin ingin menghapus catatan pengeluaran ini?')) {
      try {
        await deleteExpense(id);
        loadData();
      } catch (err) {
        alert('Gagal menghapus pengeluaran: ' + err.message);
      }
    }
  };

  // Open Edit Modal
  const handleOpenEdit = (item) => {
    setEditingExpense(item);
    setIsModalOpen(true);
  };

  // Open Add Modal
  const handleOpenAdd = () => {
    setEditingExpense(null);
    setIsModalOpen(true);
  };

  // Export to CSV
  const handleExportCSV = () => {
    if (!expenses || expenses.length === 0) {
      alert('Tidak ada data transaksi untuk di-export.');
      return;
    }

    const headers = ["ID", "Tanggal", "Nama Transaksi", "Nominal (Rp)", "Kategori", "Tipe", "Catatan"];
    const rows = expenses.map(e => [
      e.id,
      e.date,
      `"${(e.title || '').replace(/"/g, '""')}"`,
      e.amount,
      `"${e.category}"`,
      `"${e.expense_type}"`,
      `"${(e.notes || '').replace(/"/g, '""')}"`
    ]);

    const csvContent = "data:text/csv;charset=utf-8," 
      + [headers.join(","), ...rows.map(r => r.join(","))].join("\n");

    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", `Laporan_Pengeluaran_${selectedMonth}_${selectedYear}.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <div className="app-container">
      {/* Header Controls */}
      <Header
        selectedMonth={selectedMonth}
        selectedYear={selectedYear}
        onMonthChange={setSelectedMonth}
        onYearChange={setSelectedYear}
        onOpenAddModal={handleOpenAdd}
        onExportCSV={handleExportCSV}
      />

      {/* Mode Connection Info Banner */}
      <div className="demo-banner">
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <Database size={16} />
          <span>
            Status Mode Simpan Data: <strong>{isFallbackMode ? 'Demo Mode (LocalStorage Browser)' : 'Terhubung ke Backend Python FastAPI (SQLite)'}</strong>
          </span>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.4rem', color: '#94a3b8' }}>
          <Info size={14} />
          <span>Bisa dipublish di Vercel & Render secara gratis</span>
        </div>
      </div>

      {/* KPI Cards */}
      <StatCard summary={summary} />

      {/* Visual Analytics Charts */}
      <ExpenseCharts summary={summary} />

      {/* Transactions List & Filters */}
      <ExpenseTable
        expenses={expenses}
        searchQuery={searchQuery}
        onSearchChange={setSearchQuery}
        selectedCategory={selectedCategory}
        onCategoryChange={setSelectedCategory}
        selectedType={selectedType}
        onTypeChange={setSelectedType}
        onEdit={handleOpenEdit}
        onDelete={handleDelete}
      />

      {/* Form Modal */}
      <ExpenseFormModal
        isOpen={isModalOpen}
        onClose={() => {
          setIsModalOpen(false);
          setEditingExpense(null);
        }}
        onSubmit={handleFormSubmit}
        initialData={editingExpense}
      />
    </div>
  );
}
