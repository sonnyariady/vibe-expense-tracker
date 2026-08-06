import React from 'react';
import { DollarSign, TrendingUp, Calendar, PieChart } from 'lucide-react';

export function formatRupiah(number) {
  return new Intl.NumberFormat('id-ID', {
    style: 'currency',
    currency: 'IDR',
    maximumFractionDigits: 0
  }).format(number || 0);
}

export default function StatCard({ summary }) {
  const totalAmount = summary?.total_amount || 0;
  const totalCount = summary?.total_count || 0;
  const averageDaily = summary?.average_daily || 0;
  const monthlyBudget = summary?.monthly_budget || 5000000;
  
  const budgetUsagePercent = Math.min(100, Math.round((totalAmount / monthlyBudget) * 100));
  const remainingBudget = monthlyBudget - totalAmount;

  // Determine progress color
  let progressColor = 'var(--gradient-success)';
  if (budgetUsagePercent > 75 && budgetUsagePercent <= 90) {
    progressColor = 'var(--gradient-warning)';
  } else if (budgetUsagePercent > 90) {
    progressColor = 'var(--gradient-danger)';
  }

  return (
    <div className="dashboard-grid">
      {/* Total Pengeluaran */}
      <div className="stat-card">
        <div className="stat-card-header">
          <span className="stat-title">Total Pengeluaran</span>
          <div className="stat-icon-bg stat-icon-indigo">
            <DollarSign size={20} />
          </div>
        </div>
        <div className="stat-value">{formatRupiah(totalAmount)}</div>
        <div className="stat-subtext">Total bulan ini</div>
      </div>

      {/* Sisa Anggaran */}
      <div className="stat-card">
        <div className="stat-card-header">
          <span className="stat-title">Anggaran Bulanan</span>
          <div className="stat-icon-bg stat-icon-emerald">
            <TrendingUp size={20} />
          </div>
        </div>
        <div className="stat-value">{formatRupiah(monthlyBudget)}</div>
        <div className="stat-subtext">
          {remainingBudget >= 0 
            ? `Sisa: ${formatRupiah(remainingBudget)} (${100 - budgetUsagePercent}%)` 
            : `Melebihi anggaran (${formatRupiah(Math.abs(remainingBudget))})`}
        </div>
        <div className="progress-bar-bg">
          <div 
            className="progress-bar-fill" 
            style={{ 
              width: `${budgetUsagePercent}%`, 
              background: progressColor 
            }} 
          />
        </div>
      </div>

      {/* Rata-Rata Harian */}
      <div className="stat-card">
        <div className="stat-card-header">
          <span className="stat-title">Rata-Rata Harian</span>
          <div className="stat-icon-bg stat-icon-amber">
            <Calendar size={20} />
          </div>
        </div>
        <div className="stat-value">{formatRupiah(averageDaily)}</div>
        <div className="stat-subtext">Estimasi pengeluaran per hari</div>
      </div>

      {/* Total Transaksi */}
      <div className="stat-card">
        <div className="stat-card-header">
          <span className="stat-title">Jumlah Transaksi</span>
          <div className="stat-icon-bg stat-icon-rose">
            <PieChart size={20} />
          </div>
        </div>
        <div className="stat-value">{totalCount} Item</div>
        <div className="stat-subtext">Transaksi tercatat bulan ini</div>
      </div>
    </div>
  );
}
