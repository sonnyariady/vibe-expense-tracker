import React from 'react';
import { Search, Edit2, Trash2, Tag, ShoppingBag, Receipt, Coffee, Car, CreditCard, Inbox } from 'lucide-react';
import { formatRupiah } from './StatCard';
import { MASTER_CATEGORIES, MASTER_TYPES } from '../api';

export function getTypeBadgeClass(type) {
  switch ((type || '').toLowerCase()) {
    case 'belanja': return 'badge-belanja';
    case 'tagihan': return 'badge-tagihan';
    case 'jajan': return 'badge-jajan';
    case 'ongkos': return 'badge-ongkos';
    case 'topup': return 'badge-topup';
    default: return 'badge-default';
  }
}

export function getTypeIcon(type) {
  switch ((type || '').toLowerCase()) {
    case 'belanja': return <ShoppingBag size={13} />;
    case 'tagihan': return <Receipt size={13} />;
    case 'jajan': return <Coffee size={13} />;
    case 'ongkos': return <Car size={13} />;
    case 'topup': return <CreditCard size={13} />;
    default: return <Tag size={13} />;
  }
}

export function formatDateIndo(dateStr) {
  if (!dateStr) return '-';
  const date = new Date(dateStr);
  return date.toLocaleDateString('id-ID', {
    day: 'numeric',
    month: 'short',
    year: 'numeric'
  });
}

export default function ExpenseTable({
  expenses,
  searchQuery,
  onSearchChange,
  selectedCategory,
  onCategoryChange,
  selectedType,
  onTypeChange,
  onEdit,
  onDelete
}) {
  return (
    <div className="content-section">
      {/* Filter Controls */}
      <div className="filter-bar">
        <div className="search-box">
          <Search size={18} className="search-icon" />
          <input
            type="text"
            placeholder="Cari transaksi atau catatan..."
            value={searchQuery}
            onChange={(e) => onSearchChange(e.target.value)}
          />
        </div>

        <div className="filter-selects">
          <select
            className="select-filter"
            value={selectedCategory}
            onChange={(e) => onCategoryChange(e.target.value)}
          >
            <option value="">Semua Kategori</option>
            {MASTER_CATEGORIES.map((cat, i) => (
              <option key={i} value={cat}>{cat}</option>
            ))}
          </select>

          <select
            className="select-filter"
            value={selectedType}
            onChange={(e) => onTypeChange(e.target.value)}
          >
            <option value="">Semua Tipe</option>
            {MASTER_TYPES.map((t, i) => (
              <option key={i} value={t}>{t}</option>
            ))}
          </select>
        </div>
      </div>

      {/* Table List */}
      <div className="table-container">
        {expenses && expenses.length > 0 ? (
          <table className="expense-table">
            <thead>
              <tr>
                <th>Tanggal</th>
                <th>Transaksi</th>
                <th>Kategori</th>
                <th>Tipe</th>
                <th>Nominal</th>
                <th style={{ textAlign: 'center' }}>Aksi</th>
              </tr>
            </thead>
            <tbody>
              {expenses.map((item) => (
                <tr key={item.id}>
                  <td style={{ color: '#94a3b8', whiteSpace: 'nowrap' }}>
                    {formatDateIndo(item.date)}
                  </td>

                  <td>
                    <div className="expense-title">
                      <span>{item.title}</span>
                      {item.notes && <span className="expense-notes">{item.notes}</span>}
                    </div>
                  </td>

                  <td>
                    <span className="badge badge-category">
                      {item.category}
                    </span>
                  </td>

                  <td>
                    <span className={`badge ${getTypeBadgeClass(item.expense_type)}`}>
                      {getTypeIcon(item.expense_type)}
                      {item.expense_type}
                    </span>
                  </td>

                  <td className="amount-text" style={{ whiteSpace: 'nowrap' }}>
                    {formatRupiah(item.amount)}
                  </td>

                  <td style={{ textAlign: 'center', whiteSpace: 'nowrap' }}>
                    <button 
                      className="action-btn" 
                      onClick={() => onEdit(item)}
                      title="Edit Transaksi"
                    >
                      <Edit2 size={16} />
                    </button>
                    <button 
                      className="action-btn delete" 
                      onClick={() => onDelete(item.id)}
                      title="Hapus Transaksi"
                    >
                      <Trash2 size={16} />
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        ) : (
          <div className="empty-state">
            <Inbox size={48} />
            <h4>Belum Ada Data Transaksi</h4>
            <p>Tidak ditemukan pengeluaran yang sesuai dengan filter pencarian.</p>
          </div>
        )}
      </div>
    </div>
  );
}
