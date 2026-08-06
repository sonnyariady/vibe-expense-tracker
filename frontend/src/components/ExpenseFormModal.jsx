import React, { useState, useEffect } from 'react';
import { X, Check } from 'lucide-react';
import { MASTER_CATEGORIES, MASTER_TYPES } from '../api';

export default function ExpenseFormModal({ 
  isOpen, 
  onClose, 
  onSubmit, 
  initialData 
}) {
  const [title, setTitle] = useState('');
  const [amount, setAmount] = useState('');
  const [category, setCategory] = useState(MASTER_CATEGORIES[0]);
  const [expenseType, setExpenseType] = useState(MASTER_TYPES[0]);
  const [date, setDate] = useState(new Date().toISOString().split('T')[0]);
  const [notes, setNotes] = useState('');

  useEffect(() => {
    if (initialData) {
      setTitle(initialData.title || '');
      setAmount(initialData.amount || '');
      setCategory(initialData.category || MASTER_CATEGORIES[0]);
      setExpenseType(initialData.expense_type || MASTER_TYPES[0]);
      setDate(initialData.date || new Date().toISOString().split('T')[0]);
      setNotes(initialData.notes || '');
    } else {
      // Reset form
      setTitle('');
      setAmount('');
      setCategory(MASTER_CATEGORIES[0]);
      setExpenseType(MASTER_TYPES[0]);
      setDate(new Date().toISOString().split('T')[0]);
      setNotes('');
    }
  }, [initialData, isOpen]);

  if (!isOpen) return null;

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!title.trim() || !amount || Number(amount) <= 0) {
      alert('Mohon isi judul dan nominal pengeluaran secara valid.');
      return;
    }

    onSubmit({
      title: title.trim(),
      amount: Number(amount),
      category,
      expense_type: expenseType,
      date,
      notes: notes.trim()
    });
  };

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <h2>{initialData ? 'Edit Transaksi Pengeluaran' : 'Tambah Pengeluaran Baru'}</h2>
          <button className="action-btn" onClick={onClose}>
            <X size={20} />
          </button>
        </div>

        <form onSubmit={handleSubmit}>
          <div className="modal-body">
            <div className="form-group">
              <label>Nama / Judul Transaksi *</label>
              <input
                type="text"
                className="form-input"
                placeholder="Contoh: Belanja Sayuran / Bayar PLN"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                required
                autoFocus
              />
            </div>

            <div className="form-row">
              <div className="form-group">
                <label>Nominal (Rp) *</label>
                <input
                  type="number"
                  className="form-input"
                  placeholder="0"
                  min="1"
                  value={amount}
                  onChange={(e) => setAmount(e.target.value)}
                  required
                />
              </div>

              <div className="form-group">
                <label>Tanggal Transaksi *</label>
                <input
                  type="date"
                  className="form-input"
                  value={date}
                  onChange={(e) => setDate(e.target.value)}
                  required
                />
              </div>
            </div>

            <div className="form-row">
              <div className="form-group">
                <label>Kategori Pengeluaran *</label>
                <select
                  className="form-select"
                  value={category}
                  onChange={(e) => setCategory(e.target.value)}
                >
                  {MASTER_CATEGORIES.map((cat, i) => (
                    <option key={i} value={cat}>{cat}</option>
                  ))}
                </select>
              </div>

              <div className="form-group">
                <label>Tipe Pengeluaran *</label>
                <select
                  className="form-select"
                  value={expenseType}
                  onChange={(e) => setExpenseType(e.target.value)}
                >
                  {MASTER_TYPES.map((t, i) => (
                    <option key={i} value={t}>{t}</option>
                  ))}
                </select>
              </div>
            </div>

            <div className="form-group">
              <label>Catatan Tambahan (Opsional)</label>
              <textarea
                className="form-textarea"
                rows="2"
                placeholder="Contoh: Pembayaran via M-Banking / Promo Diskon 10%"
                value={notes}
                onChange={(e) => setNotes(e.target.value)}
              />
            </div>
          </div>

          <div className="modal-footer">
            <button type="button" className="btn-secondary" onClick={onClose}>
              Batal
            </button>
            <button type="submit" className="btn-primary">
              <Check size={18} />
              <span>Simpan Transaksi</span>
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
