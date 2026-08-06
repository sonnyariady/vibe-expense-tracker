// API Service Layer dengan Automatic Fallback ke LocalStorage (Demo Mode)

const API_BASE_URL = '/api';
const LOCAL_STORAGE_KEY = 'household_expenses_demo_data';

// Default Master Categories & Types
export const MASTER_CATEGORIES = [
  "Makanan & Bahan Pokok",
  "Tagihan & Utilitas",
  "Transportasi & Bensin",
  "Hiburan & Jajan",
  "Top Up & E-Wallet",
  "Kesehatan & Obat",
  "Pendidikan & Anak",
  "Perlengkapan Rumah",
  "Lain-lain"
];

export const MASTER_TYPES = [
  "Belanja",
  "Tagihan",
  "Jajan",
  "Ongkos",
  "Topup",
  "Lainnya"
];

// Initial Dummy Data for LocalStorage Fallback
const INITIAL_DUMMY_DATA = [
  {
    id: 1,
    title: "Belanja Mingguan Supermarket",
    amount: 650000,
    category: "Makanan & Bahan Pokok",
    expense_type: "Belanja",
    date: new Date().toISOString().split('T')[0],
    notes: "Sayur, daging, buah, dan beras",
    created_at: new Date().toISOString()
  },
  {
    id: 2,
    title: "Bayar Tagihan Listrik PLN",
    amount: 280000,
    category: "Tagihan & Utilitas",
    expense_type: "Tagihan",
    date: new Date(Date.now() - 86400000 * 2).toISOString().split('T')[0],
    notes: "Listrik token 200rb + admin",
    created_at: new Date().toISOString()
  },
  {
    id: 3,
    title: "Beli Bensin Mobil & Motor",
    amount: 150000,
    category: "Transportasi & Bensin",
    expense_type: "Ongkos",
    date: new Date(Date.now() - 86400000 * 3).toISOString().split('T')[0],
    notes: "Pertalite full tank",
    created_at: new Date().toISOString()
  },
  {
    id: 4,
    title: "Topup ShopeePay & GoPay",
    amount: 200000,
    category: "Top Up & E-Wallet",
    expense_type: "Topup",
    date: new Date(Date.now() - 86400000 * 4).toISOString().split('T')[0],
    notes: "Untuk persediaan belanja online",
    created_at: new Date().toISOString()
  },
  {
    id: 5,
    title: "Jajan Kopi & Boba",
    amount: 45000,
    category: "Hiburan & Jajan",
    expense_type: "Jajan",
    date: new Date(Date.now() - 86400000 * 1).toISOString().split('T')[0],
    notes: "Kopi kekinian bersama keluarga",
    created_at: new Date().toISOString()
  },
  {
    id: 6,
    title: "Tagihan Wi-Fi IndiHome",
    amount: 350000,
    category: "Tagihan & Utilitas",
    expense_type: "Tagihan",
    date: new Date(Date.now() - 86400000 * 5).toISOString().split('T')[0],
    notes: "Paket 30 Mbps",
    created_at: new Date().toISOString()
  }
];

// Helper to get LocalStorage Data
function getLocalExpenses() {
  const stored = localStorage.getItem(LOCAL_STORAGE_KEY);
  if (!stored) {
    localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(INITIAL_DUMMY_DATA));
    return INITIAL_DUMMY_DATA;
  }
  try {
    return JSON.parse(stored);
  } catch (e) {
    return INITIAL_DUMMY_DATA;
  }
}

// Helper to save LocalStorage Data
function saveLocalExpenses(data) {
  localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(data));
}

// API Functions with automatic fallback
export async function fetchExpenses(params = {}) {
  const { month, year, category, expense_type, search } = params;
  
  try {
    const queryParams = new URLSearchParams();
    if (month) queryParams.append('month', month);
    if (year) queryParams.append('year', year);
    if (category) queryParams.append('category', category);
    if (expense_type) queryParams.append('expense_type', expense_type);
    if (search) queryParams.append('search', search);

    const res = await fetch(`${API_BASE_URL}/expenses?${queryParams.toString()}`);
    if (!res.ok) throw new Error('API server error');
    const data = await res.json();
    return { data, isFallback: false };
  } catch (err) {
    // Fallback LocalStorage Mode
    let items = getLocalExpenses();
    
    if (year) {
      items = items.filter(item => new Date(item.date).getFullYear() === parseInt(year));
    }
    if (month) {
      items = items.filter(item => (new Date(item.date).getMonth() + 1) === parseInt(month));
    }
    if (category) {
      items = items.filter(item => item.category === category);
    }
    if (expense_type) {
      items = items.filter(item => item.expense_type === expense_type);
    }
    if (search) {
      const q = search.toLowerCase();
      items = items.filter(item => 
        item.title.toLowerCase().includes(q) || 
        (item.notes && item.notes.toLowerCase().includes(q))
      );
    }

    items.sort((a, b) => new Date(b.date) - new Date(a.date));
    return { data: items, isFallback: true };
  }
}

export async function createExpense(payload) {
  try {
    const res = await fetch(`${API_BASE_URL}/expenses`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    if (!res.ok) throw new Error('API create error');
    const data = await res.json();
    return { data, isFallback: false };
  } catch (err) {
    // LocalStorage Fallback
    const items = getLocalExpenses();
    const newItem = {
      ...payload,
      id: Date.now(),
      created_at: new Date().toISOString()
    };
    items.unshift(newItem);
    saveLocalExpenses(items);
    return { data: newItem, isFallback: true };
  }
}

export async function updateExpense(id, payload) {
  try {
    const res = await fetch(`${API_BASE_URL}/expenses/${id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    if (!res.ok) throw new Error('API update error');
    const data = await res.json();
    return { data, isFallback: false };
  } catch (err) {
    let items = getLocalExpenses();
    const idx = items.findIndex(item => item.id === id);
    if (idx !== -1) {
      items[idx] = { ...items[idx], ...payload };
      saveLocalExpenses(items);
      return { data: items[idx], isFallback: true };
    }
    throw new Error('Item not found');
  }
}

export async function deleteExpense(id) {
  try {
    const res = await fetch(`${API_BASE_URL}/expenses/${id}`, {
      method: 'DELETE'
    });
    if (!res.ok) throw new Error('API delete error');
    return { success: true, isFallback: false };
  } catch (err) {
    let items = getLocalExpenses();
    items = items.filter(item => item.id !== id);
    saveLocalExpenses(items);
    return { success: true, isFallback: true };
  }
}

export async function fetchSummary(params = {}) {
  const { month, year } = params;
  const targetMonth = month ? parseInt(month) : new Date().getMonth() + 1;
  const targetYear = year ? parseInt(year) : new Date().getFullYear();

  try {
    const queryParams = new URLSearchParams();
    if (month) queryParams.append('month', month);
    if (year) queryParams.append('year', year);

    const res = await fetch(`${API_BASE_URL}/summary?${queryParams.toString()}`);
    if (!res.ok) throw new Error('API summary error');
    const data = await res.json();
    return { data, isFallback: false };
  } catch (err) {
    // LocalStorage summary calculation
    const allItems = getLocalExpenses();
    const items = allItems.filter(item => {
      const d = new Date(item.date);
      return d.getFullYear() === targetYear && (d.getMonth() + 1) === targetMonth;
    });

    const total_amount = items.reduce((sum, i) => sum + Number(i.amount), 0);
    const total_count = items.length;
    const now = new Date();
    const daysElapsed = (now.getFullYear() === targetYear && (now.getMonth() + 1) === targetMonth)
      ? Math.max(1, now.getDate())
      : 30;
    const average_daily = Math.round(total_amount / daysElapsed);

    // Group by Category
    const catMap = {};
    items.forEach(item => {
      catMap[item.category] = (catMap[item.category] || 0) + Number(item.amount);
    });

    const by_category = MASTER_CATEGORIES.map(cat => {
      const total = catMap[cat] || 0;
      return {
        category: cat,
        total,
        percentage: total_amount > 0 ? Number((total / total_amount * 100).toFixed(1)) : 0,
        count: items.filter(i => i.category === cat).length
      };
    }).filter(c => c.total > 0).sort((a, b) => b.total - a.total);

    // Group by Type
    const typeMap = {};
    items.forEach(item => {
      typeMap[item.expense_type] = (typeMap[item.expense_type] || 0) + Number(item.amount);
    });

    const by_type = MASTER_TYPES.map(t => {
      const total = typeMap[t] || 0;
      return {
        expense_type: t,
        total,
        percentage: total_amount > 0 ? Number((total / total_amount * 100).toFixed(1)) : 0,
        count: items.filter(i => i.expense_type === t).length
      };
    }).filter(t => t.total > 0).sort((a, b) => b.total - a.total);

    return {
      data: {
        total_amount,
        total_count,
        average_daily,
        monthly_budget: 5000000,
        by_category,
        by_type
      },
      isFallback: true
    };
  }
}
