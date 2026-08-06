import React from 'react';
import { 
  PieChart, Pie, Cell, ResponsiveContainer, Tooltip, Legend,
  BarChart, Bar, XAxis, YAxis, CartesianGrid
} from 'recharts';
import { PieChart as PieIcon, BarChart3 } from 'lucide-react';
import { formatRupiah } from './StatCard';

const COLORS = [
  '#6366f1', '#10b981', '#f59e0b', '#f43f5e', 
  '#06b6d4', '#a855f7', '#ec4899', '#3b82f6', '#84cc16'
];

export default function ExpenseCharts({ summary }) {
  const byCategory = summary?.by_category || [];
  const byType = summary?.by_type || [];

  const CustomTooltip = ({ active, payload }) => {
    if (active && payload && payload.length) {
      const data = payload[0].payload;
      return (
        <div style={{
          background: '#1e293b',
          border: '1px solid rgba(255,255,255,0.1)',
          padding: '0.6rem 0.9rem',
          borderRadius: '8px',
          boxShadow: '0 4px 12px rgba(0,0,0,0.3)',
          fontSize: '0.825rem'
        }}>
          <p style={{ fontWeight: 700, color: '#f8fafc', marginBottom: '0.2rem' }}>
            {data.category || data.expense_type}
          </p>
          <p style={{ color: '#a5b4fc', fontWeight: 600 }}>
            {formatRupiah(data.total)} ({data.percentage}%)
          </p>
          <p style={{ color: '#94a3b8', fontSize: '0.75rem' }}>
            {data.count} transaksi
          </p>
        </div>
      );
    }
    return null;
  };

  return (
    <div className="analytics-section">
      {/* Category Pie/Donut Chart */}
      <div className="chart-card">
        <div className="chart-card-title">
          <h3>
            <PieIcon size={20} style={{ color: '#818cf8' }} />
            Distribusi Per Kategori
          </h3>
        </div>
        <div className="chart-container">
          {byCategory.length > 0 ? (
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie
                  data={byCategory}
                  cx="50%"
                  cy="50%"
                  innerRadius={55}
                  outerRadius={85}
                  paddingAngle={4}
                  dataKey="total"
                  nameKey="category"
                >
                  {byCategory.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                  ))}
                </Pie>
                <Tooltip content={<CustomTooltip />} />
                <Legend 
                  verticalAlign="bottom" 
                  height={36} 
                  iconType="circle"
                  formatter={(value) => <span style={{ color: '#cbd5e1', fontSize: '0.75rem' }}>{value}</span>}
                />
              </PieChart>
            </ResponsiveContainer>
          ) : (
            <div style={{ color: '#64748b', fontSize: '0.875rem' }}>Belum ada data pengeluaran bulan ini</div>
          )}
        </div>
      </div>

      {/* Type Bar Chart */}
      <div className="chart-card">
        <div className="chart-card-title">
          <h3>
            <BarChart3 size={20} style={{ color: '#34d399' }} />
            Tipe Pengeluaran (Belanja, Tagihan, Ongkos, dll)
          </h3>
        </div>
        <div className="chart-container">
          {byType.length > 0 ? (
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={byType} margin={{ top: 10, right: 10, left: 10, bottom: 25 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.05)" />
                <XAxis 
                  dataKey="expense_type" 
                  stroke="#94a3b8" 
                  fontSize={11}
                  tickLine={false}
                />
                <YAxis 
                  stroke="#94a3b8" 
                  fontSize={11}
                  tickFormatter={(val) => `${val / 1000}k`}
                  tickLine={false}
                />
                <Tooltip content={<CustomTooltip />} />
                <Bar 
                  dataKey="total" 
                  fill="#6366f1" 
                  radius={[6, 6, 0, 0]}
                  barSize={32}
                >
                  {byType.map((entry, index) => (
                    <Cell key={`bar-${index}`} fill={COLORS[index % COLORS.length]} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          ) : (
            <div style={{ color: '#64748b', fontSize: '0.875rem' }}>Belum ada data pengeluaran bulan ini</div>
          )}
        </div>
      </div>
    </div>
  );
}
