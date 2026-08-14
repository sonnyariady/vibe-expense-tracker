import os
import base64
import subprocess

BASE_DIR = r"c:\Latihan\Fullstack\PengeluaranBulanan"
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "docs", "screenshots")

def get_base64_image(image_filename):
    path = os.path.join(SCREENSHOTS_DIR, image_filename)
    if os.path.exists(path):
        with open(path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode('utf-8')
            return f"data:image/png;base64,{encoded}"
    return ""

# Load base64 strings of screenshots
img_header = get_base64_image("01_header_period_navigation.png")
img_kpi = get_base64_image("02_kpi_dashboard.png")
img_analytics = get_base64_image("03_visual_analytics.png")
img_modal = get_base64_image("04_add_expense_modal.png")
img_filters = get_base64_image("05_filters_and_search.png")
img_action = get_base64_image("06_action_edit_delete.png")
img_export = get_base64_image("07_export_csv.png")

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Vibecoding Portfolio - Household Expense Tracker</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

  @page {{
    size: 1920px 1080px;
    margin: 0;
  }}

  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}

  body {{
    width: 1920px;
    background-color: #07090E;
    color: #F1F5F9;
    font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}

  .slide {{
    width: 1920px;
    height: 1080px;
    page-break-after: always;
    page-break-inside: avoid;
    padding: 60px 80px;
    position: relative;
    background: radial-gradient(circle at 5% 5%, rgba(16, 185, 129, 0.12), transparent 45%),
                radial-gradient(circle at 95% 95%, rgba(99, 102, 241, 0.12), transparent 45%),
                #080C14;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    overflow: hidden;
  }}

  /* Header Bar */
  .slide-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    padding-bottom: 20px;
  }}

  .brand-badge {{
    display: flex;
    align-items: center;
    gap: 12px;
  }}

  .brand-logo {{
    width: 36px;
    height: 36px;
    background: linear-gradient(135deg, #10B981, #059669);
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    font-size: 20px;
    color: white;
    box-shadow: 0 0 15px rgba(16, 185, 129, 0.4);
  }}

  .brand-title {{
    font-size: 20px;
    font-weight: 700;
    letter-spacing: -0.5px;
    color: #F8FAFC;
  }}

  .vibe-tag {{
    background: rgba(16, 185, 129, 0.15);
    border: 1px solid rgba(16, 185, 129, 0.4);
    color: #34D399;
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.5px;
    text-transform: uppercase;
  }}

  .slide-number {{
    font-size: 15px;
    font-weight: 600;
    color: #64748B;
  }}

  /* Title Styling */
  .title-group {{
    margin-top: 15px;
  }}

  .slide-title {{
    font-size: 42px;
    font-weight: 800;
    letter-spacing: -1px;
    background: linear-gradient(135deg, #FFFFFF 30%, #94A3B8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    line-height: 1.2;
  }}

  .slide-subtitle {{
    font-size: 20px;
    color: #94A3B8;
    margin-top: 8px;
    font-weight: 400;
  }}

  /* Content Containers */
  .content-body {{
    flex: 1;
    margin-top: 25px;
    margin-bottom: 25px;
    display: flex;
    gap: 40px;
  }}

  .grid-2 {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 40px;
    width: 100%;
  }}

  .grid-3 {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 30px;
    width: 100%;
  }}

  /* Glass Cards */
  .glass-card {{
    background: rgba(15, 23, 42, 0.65);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 20px;
    padding: 30px;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
    backdrop-filter: blur(12px);
    display: flex;
    flex-direction: column;
  }}

  .card-highlight {{
    border-color: rgba(16, 185, 129, 0.3);
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.06), rgba(15, 23, 42, 0.7));
  }}

  .card-header {{
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 18px;
  }}

  .card-icon {{
    width: 44px;
    height: 44px;
    border-radius: 12px;
    background: rgba(16, 185, 129, 0.15);
    border: 1px solid rgba(16, 185, 129, 0.3);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
  }}

  .card-title {{
    font-size: 22px;
    font-weight: 700;
    color: #F8FAFC;
  }}

  .card-text {{
    font-size: 16px;
    color: #CBD5E1;
    line-height: 1.6;
  }}

  /* Bullet points */
  .feature-list {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 14px;
  }}

  .feature-list li {{
    display: flex;
    align-items: flex-start;
    gap: 12px;
    font-size: 16px;
    color: #CBD5E1;
    line-height: 1.5;
  }}

  .feature-list li::before {{
    content: "✓";
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-width: 22px;
    height: 22px;
    background: rgba(16, 185, 129, 0.2);
    color: #34D399;
    border-radius: 50%;
    font-weight: 800;
    font-size: 12px;
    margin-top: 2px;
  }}

  /* Code block */
  .code-box {{
    background: #030712;
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 14px;
    padding: 20px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 14px;
    color: #38BDF8;
    line-height: 1.6;
    overflow: hidden;
  }}

  .code-comment {{
    color: #64748B;
  }}

  .code-cmd {{
    color: #34D399;
  }}

  /* Images */
  .img-frame {{
    width: 100%;
    border-radius: 16px;
    border: 1px solid rgba(255, 255, 255, 0.12);
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.5);
    object-fit: cover;
  }}

  /* Footer */
  .slide-footer {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    padding-top: 16px;
  }}

  .footer-text {{
    font-size: 14px;
    color: #64748B;
    display: flex;
    align-items: center;
    gap: 8px;
  }}

  .footer-dot {{
    width: 6px;
    height: 6px;
    background: #10B981;
    border-radius: 50%;
  }}

  /* Metric Badges */
  .kpi-row {{
    display: flex;
    gap: 20px;
    margin-top: 20px;
  }}

  .kpi-badge {{
    flex: 1;
    background: rgba(30, 41, 59, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 14px;
    padding: 16px 20px;
    text-align: center;
  }}

  .kpi-val {{
    font-size: 28px;
    font-weight: 800;
    color: #34D399;
  }}

  .kpi-lbl {{
    font-size: 13px;
    color: #94A3B8;
    margin-top: 4px;
    font-weight: 500;
  }}

  /* Cover Slide Custom Style */
  .cover-slide {{
    justify-content: center;
    align-items: center;
    text-align: center;
    background: radial-gradient(circle at 50% 40%, rgba(16, 185, 129, 0.18), transparent 60%),
                radial-gradient(circle at 80% 80%, rgba(99, 102, 241, 0.15), transparent 50%),
                #07090E;
  }}

  .cover-badge {{
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: rgba(16, 185, 129, 0.12);
    border: 1px solid rgba(16, 185, 129, 0.4);
    color: #34D399;
    padding: 10px 24px;
    border-radius: 30px;
    font-size: 16px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 25px;
    box-shadow: 0 0 25px rgba(16, 185, 129, 0.25);
  }}

  .cover-title {{
    font-size: 68px;
    font-weight: 800;
    line-height: 1.1;
    letter-spacing: -2px;
    background: linear-gradient(135deg, #FFFFFF 20%, #CBD5E1 60%, #10B981 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    max-width: 1400px;
  }}

  .cover-sub {{
    font-size: 26px;
    color: #94A3B8;
    max-width: 1100px;
    margin-top: 25px;
    line-height: 1.5;
    font-weight: 400;
  }}

  .cover-tech-pills {{
    display: flex;
    gap: 15px;
    margin-top: 45px;
  }}

  .tech-pill {{
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.12);
    padding: 10px 22px;
    border-radius: 12px;
    font-size: 15px;
    font-weight: 600;
    color: #E2E8F0;
  }}
</style>
</head>
<body>

<!-- SLIDE 1: COVER -->
<div class="slide cover-slide">
  <div>
    <div class="cover-badge">
      ⚡ Vibecoding Portfolio Showcase
    </div>
    <h1 class="cover-title">Household Expense Tracker</h1>
    <p class="cover-sub">
      A Modern Full-Stack Financial Management Web Application built from scratch using 
      <strong>AI Pair Programming & Vibecoding</strong>.
    </p>

    <div style="display: flex; justify-content: center;">
      <div class="cover-tech-pills">
        <span class="tech-pill">🐍 Python FastAPI</span>
        <span class="tech-pill">🗄️ SQLite & SQLAlchemy</span>
        <span class="tech-pill">⚛️ React 18 & Vite</span>
        <span class="tech-pill">📊 Recharts & Glassmorphism</span>
        <span class="tech-pill">💾 Dual-Storage Engine</span>
      </div>
    </div>
  </div>

  <div class="slide-footer" style="width: 100%; max-width: 1400px; margin-top: 60px;">
    <div class="footer-text">
      <span class="footer-dot"></span> Built with AI Agent Pair Programming
    </div>
    <div class="footer-text">
      Swipe to Explore Project Case Study & Manual →
    </div>
  </div>
</div>

<!-- SLIDE 2: EXECUTIVE SUMMARY & VIBECODING APPROACH -->
<div class="slide">
  <div class="slide-header">
    <div class="brand-badge">
      <div class="brand-logo">V</div>
      <div class="brand-title">Vibecoding Case Study</div>
      <span class="vibe-tag">10x Speed</span>
    </div>
    <div class="slide-number">Slide 02 / 09</div>
  </div>

  <div class="title-group">
    <h2 class="slide-title">Executive Summary & The Vibecoding Workflow</h2>
    <p class="slide-subtitle">How natural language intent turned into a robust production-ready web app in record time.</p>
  </div>

  <div class="content-body grid-2">
    <div class="glass-card card-highlight">
      <div class="card-header">
        <div class="card-icon">🚀</div>
        <div class="card-title">What is Vibecoding?</div>
      </div>
      <p class="card-text" style="margin-bottom: 20px;">
        Vibecoding is an iterative AI-first development methodology where developers express architecture, requirements, and UI aesthetics in high-level natural language prompt sequences while AI handles code generation, debugging, refactoring, and documentation.
      </p>
      <ul class="feature-list">
        <li><strong>Zero Boilerplate Drag:</strong> Full FastAPI REST backend + React Vite frontend structured in minutes.</li>
        <li><strong>Iterative Refinement:</strong> Instant feedback loops for complex features like budget alerts and charts.</li>
        <li><strong>Automatic Documentation:</strong> Auto-generated READMEs, OpenAPI specs, and user manuals.</li>
      </ul>
    </div>

    <div class="glass-card">
      <div class="card-header">
        <div class="card-icon">💡</div>
        <div class="card-title">Project Objectives & Value</div>
      </div>
      <p class="card-text" style="margin-bottom: 16px;">
        Designed to solve household financial clutter with clear monthly budget limits, instant categorization, real-time KPI analytics, and zero-latency filtering.
      </p>
      
      <div class="kpi-row">
        <div class="kpi-badge">
          <div class="kpi-val">100%</div>
          <div class="kpi-lbl">Full-Stack Coverage</div>
        </div>
        <div class="kpi-badge">
          <div class="kpi-val">2 Mode</div>
          <div class="kpi-lbl">Storage Architecture</div>
        </div>
        <div class="kpi-badge">
          <div class="kpi-val">&lt; 100ms</div>
          <div class="kpi-lbl">Search & Filter Speed</div>
        </div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div class="footer-text"><span class="footer-dot"></span> Household Expense Tracker Portfolio</div>
    <div class="footer-text">Vibecoding Methodology • Modern Full-Stack Development</div>
  </div>
</div>

<!-- SLIDE 3: TECH STACK & ARCHITECTURE -->
<div class="slide">
  <div class="slide-header">
    <div class="brand-badge">
      <div class="brand-logo">V</div>
      <div class="brand-title">System Architecture</div>
      <span class="vibe-tag">Tech Stack</span>
    </div>
    <div class="slide-number">Slide 03 / 09</div>
  </div>

  <div class="title-group">
    <h2 class="slide-title">Full-Stack Architecture & Data Flow</h2>
    <p class="slide-subtitle">Modular, decoupled architecture with persistent backend storage & static fallback.</p>
  </div>

  <div class="content-body grid-2">
    <div class="glass-card">
      <div class="card-header">
        <div class="card-icon">⚙️</div>
        <div class="card-title">Backend Architecture (Python FastAPI)</div>
      </div>
      <ul class="feature-list" style="margin-bottom: 20px;">
        <li><strong>FastAPI Framework:</strong> Asynchronous high-performance REST API endpoints.</li>
        <li><strong>Pydantic v2 Schemas:</strong> Strict data validation for entry creation, updates, & responses.</li>
        <li><strong>SQLAlchemy ORM:</strong> Clean Object-Relational Mapping interfacing with SQLite database.</li>
        <li><strong>Interactive Swagger Specs:</strong> OpenAPI documentation pre-configured at <code>/docs</code>.</li>
      </ul>
      <div class="code-box">
        <span class="code-comment"># API Endpoint Definition (main.py)</span><br>
        <span class="code-cmd">@app.get</span>("/api/expenses", response_model=List[schemas.Expense])<br>
        <span class="code-cmd">def</span> get_expenses(month: int, year: int, db: Session = Depends(get_db)):<br>
        &nbsp;&nbsp;return db.query(Expense).filter(...).all()
      </div>
    </div>

    <div class="glass-card">
      <div class="card-header">
        <div class="card-icon">🎨</div>
        <div class="card-title">Frontend Architecture (React 18 + Vite)</div>
      </div>
      <ul class="feature-list" style="margin-bottom: 20px;">
        <li><strong>React 18 & Vite:</strong> Ultra-fast HMR and modern JSX component rendering.</li>
        <li><strong>Recharts Library:</strong> Interactive Donut & Bar chart visual analytics.</li>
        <li><strong>Lucide React Icons:</strong> Vector icon design system for UI actions.</li>
        <li><strong>Glassmorphism Theme:</strong> Sleek dark mode glass UI styled using custom modern CSS.</li>
      </ul>
      <div class="code-box">
        <span class="code-comment">// Dual API Layer with LocalStorage Fallback</span><br>
        <span class="code-cmd">export const</span> fetchExpenses = <span class="code-cmd">async</span> (month, year) =&gt; &#123;<br>
        &nbsp;&nbsp;<span class="code-cmd">if</span> (isBackendAvailable) <span class="code-cmd">return</span> axios.get(`/api/expenses`);<br>
        &nbsp;&nbsp;<span class="code-cmd">return</span> getLocalStorageExpenses(month, year);<br>
        &#125;;
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div class="footer-text"><span class="footer-dot"></span> Household Expense Tracker Portfolio</div>
    <div class="footer-text">FastAPI • SQLite • React 18 • Recharts • Vite</div>
  </div>
</div>

<!-- SLIDE 4: DASHBOARD & KPI ANALYTICS -->
<div class="slide">
  <div class="slide-header">
    <div class="brand-badge">
      <div class="brand-logo">V</div>
      <div class="brand-title">User Interface Showcase</div>
      <span class="vibe-tag">KPI Analytics</span>
    </div>
    <div class="slide-number">Slide 04 / 09</div>
  </div>

  <div class="title-group">
    <h2 class="slide-title">Interactive Dashboard & Smart Budget Engine</h2>
    <p class="slide-subtitle">Real-time financial metrics with automated color-coded alert indicators.</p>
  </div>

  <div class="content-body grid-2">
    <div style="display: flex; flex-direction: column; gap: 20px;">
      <img src="{img_kpi}" class="img-frame" alt="KPI Dashboard">
      <img src="{img_header}" class="img-frame" alt="Header Navigation">
    </div>

    <div class="glass-card card-highlight">
      <div class="card-header">
        <div class="card-icon">📊</div>
        <div class="card-title">Key Dashboard Features</div>
      </div>
      <ul class="feature-list">
        <li><strong>Total Expense Card:</strong> Instant sum calculation formatted in Indonesian Rupiah (IDR).</li>
        <li><strong>Dynamic Budget Progress Bar:</strong> Automatic visual alert threshold:
          <br>&bull; <span style="color:#34D399; font-weight:700;">Green</span> (&lt; 75% used): Safe spending rate.
          <br>&bull; <span style="color:#FBBF24; font-weight:700;">Yellow</span> (75% - 100%): Budget warning limit.
          <br>&bull; <span style="color:#F87171; font-weight:700;">Red Alert</span> (&gt; 100%): Over-budget notification.
        </li>
        <li><strong>Daily Average Spending:</strong> Automated estimation of expenditure per calendar day.</li>
        <li><strong>Month & Year Period Switcher:</strong> Instant switching between historical monthly reports.</li>
      </ul>
    </div>
  </div>

  <div class="slide-footer">
    <div class="footer-text"><span class="footer-dot"></span> Household Expense Tracker Portfolio</div>
    <div class="footer-text">Real-Time Financial Dashboard • Budget Alert System</div>
  </div>
</div>

<!-- SLIDE 5: VISUAL CHARTS & CATEGORY BREAKDOWN -->
<div class="slide">
  <div class="slide-header">
    <div class="brand-badge">
      <div class="brand-logo">V</div>
      <div class="brand-title">Data Visualization</div>
      <span class="vibe-tag">Visual Charts</span>
    </div>
    <div class="slide-number">Slide 05 / 09</div>
  </div>

  <div class="title-group">
    <h2 class="slide-title">Visual Expense Analytics & Category Breakdown</h2>
    <p class="slide-subtitle">Transform raw numbers into actionable graphical spending insights.</p>
  </div>

  <div class="content-body grid-2">
    <div class="glass-card">
      <div class="card-header">
        <div class="card-icon">📈</div>
        <div class="card-title">Graphical Insights (Recharts)</div>
      </div>
      <ul class="feature-list" style="margin-bottom: 20px;">
        <li><strong>Category Donut Chart:</strong> Displays percentage allocation across Groceries, Utilities, Transit, Entertainment, Top-Ups, & Education.</li>
        <li><strong>Expense Type Bar Chart:</strong> Compares spending volume across Shopping vs Bills vs Snacks vs Transit.</li>
        <li><strong>Interactive Tooltips:</strong> Hover over chart segments to inspect exact totals and counts.</li>
      </ul>
      <div class="kpi-badge" style="text-align: left; padding: 18px;">
        <span style="font-size: 14px; color: #94A3B8;">Supported Expense Categories:</span>
        <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px;">
          <span style="background:rgba(255,255,255,0.08); padding:4px 10px; border-radius:6px; font-size:13px;">🛒 Groceries</span>
          <span style="background:rgba(255,255,255,0.08); padding:4px 10px; border-radius:6px; font-size:13px;">💡 Utilities</span>
          <span style="background:rgba(255,255,255,0.08); padding:4px 10px; border-radius:6px; font-size:13px;">🚗 Transport</span>
          <span style="background:rgba(255,255,255,0.08); padding:4px 10px; border-radius:6px; font-size:13px;">🍿 Entertainment</span>
          <span style="background:rgba(255,255,255,0.08); padding:4px 10px; border-radius:6px; font-size:13px;">💳 Top Up</span>
        </div>
      </div>
    </div>

    <div>
      <img src="{img_analytics}" class="img-frame" alt="Visual Analytics Charts">
    </div>
  </div>

  <div class="slide-footer">
    <div class="footer-text"><span class="footer-dot"></span> Household Expense Tracker Portfolio</div>
    <div class="footer-text">Recharts Analytics • Donut & Bar Chart Visualizations</div>
  </div>
</div>

<!-- SLIDE 6: USER MANUAL & STEP-BY-STEP GUIDE -->
<div class="slide">
  <div class="slide-header">
    <div class="brand-badge">
      <div class="brand-logo">V</div>
      <div class="brand-title">User Manual</div>
      <span class="vibe-tag">Workflow Guide</span>
    </div>
    <div class="slide-number">Slide 06 / 09</div>
  </div>

  <div class="title-group">
    <h2 class="slide-title">User Manual & Daily Operations Guide</h2>
    <p class="slide-subtitle">Simple, intuitive workflow for logging, filtering, and exporting transactions.</p>
  </div>

  <div class="content-body grid-3">
    <div class="glass-card">
      <div class="card-header">
        <div class="card-icon">➕</div>
        <div class="card-title">1. Add Expense</div>
      </div>
      <p class="card-text" style="font-size:14px; margin-bottom:12px;">
        Click <strong>"+ Tambah Pengeluaran"</strong> button to open the modal form. Fill in Title, Amount, Date, Category, and Type.
      </p>
      <img src="{img_modal}" class="img-frame" alt="Add Expense Modal" style="max-height: 220px; object-fit: contain;">
    </div>

    <div class="glass-card">
      <div class="card-header">
        <div class="card-icon">🔍</div>
        <div class="card-title">2. Search & Filter</div>
      </div>
      <p class="card-text" style="font-size:14px; margin-bottom:12px;">
        Filter instantly by keyword search, category dropdown, or expense type to locate specific transaction entries.
      </p>
      <img src="{img_filters}" class="img-frame" alt="Filters and Search" style="max-height: 220px; object-fit: contain;">
    </div>

    <div class="glass-card">
      <div class="card-header">
        <div class="card-icon">📥</div>
        <div class="card-title">3. Export to CSV</div>
      </div>
      <p class="card-text" style="font-size:14px; margin-bottom:12px;">
        Click <strong>"Export CSV"</strong> to generate downloadable financial reports ready for Excel or Google Sheets.
      </p>
      <img src="{img_export}" class="img-frame" alt="Export CSV" style="max-height: 220px; object-fit: contain;">
    </div>
  </div>

  <div class="slide-footer">
    <div class="footer-text"><span class="footer-dot"></span> Household Expense Tracker Portfolio</div>
    <div class="footer-text">Step-by-Step User Manual • Easy Operations</div>
  </div>
</div>

<!-- SLIDE 7: DUAL-STORAGE ARCHITECTURE & RESILIENCE -->
<div class="slide">
  <div class="slide-header">
    <div class="brand-badge">
      <div class="brand-logo">V</div>
      <div class="brand-title">Engineering Highlight</div>
      <span class="vibe-tag">Resilient Design</span>
    </div>
    <div class="slide-number">Slide 07 / 09</div>
  </div>

  <div class="title-group">
    <h2 class="slide-title">Dual-Storage Engine: Server Persistence & Offline Fallback</h2>
    <p class="slide-subtitle">Guaranteed seamless availability whether backend server is connected or offline.</p>
  </div>

  <div class="content-body grid-2">
    <div class="glass-card card-highlight">
      <div class="card-header">
        <div class="card-icon">⚡</div>
        <div class="card-title">How Dual-Storage Engine Works</div>
      </div>
      <ul class="feature-list">
        <li><strong>Backend Active (FastAPI + SQLite):</strong> Full REST API persistence. All transaction CRUD operations sync with local SQLite database file.</li>
        <li><strong>Offline / Static Demo Mode:</strong> If backend server is offline, the React app automatically detects state and switches to <code>LocalStorage</code> mode.</li>
        <li><strong>Zero Downtime Demo:</strong> Enables static hosting on GitHub Pages or Vercel without requiring an active server instance!</li>
      </ul>
      <div class="code-box" style="margin-top: 15px;">
        <span class="code-comment">// Automatic Health Check & Failover</span><br>
        <span class="code-cmd">const</span> checkBackendHealth = <span class="code-cmd">async</span> () =&gt; &#123;<br>
        &nbsp;&nbsp;<span class="code-cmd">try</span> &#123;<br>
        &nbsp;&nbsp;&nbsp;&nbsp;<span class="code-cmd">await</span> axios.get('/api/health');<br>
        &nbsp;&nbsp;&nbsp;&nbsp;setMode('<span style="color:#34D399">FASTAPI_SQLITE</span>');<br>
        &nbsp;&nbsp;&#125; <span class="code-cmd">catch</span> &#123;<br>
        &nbsp;&nbsp;&nbsp;&nbsp;setMode('<span style="color:#FBBF24">DEMO_LOCALSTORAGE</span>');<br>
        &nbsp;&nbsp;&#125;<br>
        &#125;;
      </div>
    </div>

    <div>
      <img src="{img_action}" class="img-frame" alt="Action Edit Delete Table" style="margin-bottom: 20px;">
      <div class="glass-card" style="padding: 20px;">
        <div style="font-size: 16px; font-weight:700; color:#34D399; margin-bottom:8px;">
          🟢 Connected Status Banner
        </div>
        <p style="font-size:14px; color:#94A3B8;">
          Header dynamically displays active connection mode: <strong>"Terhubung ke Server FastAPI (SQLite)"</strong> vs <strong>"Demo Mode (LocalStorage)"</strong>.
        </p>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div class="footer-text"><span class="footer-dot"></span> Household Expense Tracker Portfolio</div>
    <div class="footer-text">Dual-Storage Mode • Transparent Client Failover</div>
  </div>
</div>

<!-- SLIDE 8: QUICK START & DEPLOYMENT -->
<div class="slide">
  <div class="slide-header">
    <div class="brand-badge">
      <div class="brand-logo">V</div>
      <div class="brand-title">Developer Experience</div>
      <span class="vibe-tag">Quick Start</span>
    </div>
    <div class="slide-number">Slide 08 / 09</div>
  </div>

  <div class="title-group">
    <h2 class="slide-title">Local Setup & Deployment Options</h2>
    <p class="slide-subtitle">Simple commands to launch locally or deploy free to cloud platforms.</p>
  </div>

  <div class="content-body grid-2">
    <div class="glass-card">
      <div class="card-header">
        <div class="card-icon">🖥️</div>
        <div class="card-title">Local Development Setup</div>
      </div>
      <div class="code-box" style="margin-bottom: 15px;">
        <span class="code-comment"># 1. Start Python FastAPI Backend</span><br>
        <span class="code-cmd">cd</span> backend<br>
        <span class="code-cmd">.\venv\Scripts\activate</span><br>
        <span class="code-cmd">pip install</span> -r requirements.txt<br>
        <span class="code-cmd">uvicorn</span> main:app --reload --port 8000
      </div>
      <div class="code-box">
        <span class="code-comment"># 2. Start React Vite Frontend</span><br>
        <span class="code-cmd">cd</span> frontend<br>
        <span class="code-cmd">npm install</span><br>
        <span class="code-cmd">npm run dev</span>
      </div>
    </div>

    <div class="glass-card card-highlight">
      <div class="card-header">
        <div class="card-icon">☁️</div>
        <div class="card-title">Free Cloud Deployment</div>
      </div>
      <ul class="feature-list" style="margin-bottom: 20px;">
        <li><strong>Backend (Render.com):</strong> Deploy <code>backend/</code> folder as a free Python Web Service with SQLite persistence.</li>
        <li><strong>Frontend (Vercel / Netlify):</strong> Host <code>frontend/</code> SPA web app with instant global CDN distribution.</li>
        <li><strong>Static Demo (GitHub Pages):</strong> Zero-cost static hosting taking full advantage of LocalStorage fallback.</li>
      </ul>
      <div style="background: rgba(16,185,129,0.12); padding: 16px; border-radius: 12px; border: 1px solid rgba(16,185,129,0.3);">
        <strong style="color:#34D399; font-size:15px;">💡 Open Source Repository:</strong>
        <p style="font-size:14px; color:#CBD5E1; margin-top:4px;">
          Includes step-by-step documentation, database seeds, and test setup.
        </p>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div class="footer-text"><span class="footer-dot"></span> Household Expense Tracker Portfolio</div>
    <div class="footer-text">Render.com • Vercel • GitHub Pages • Docker Ready</div>
  </div>
</div>

<!-- SLIDE 9: KEY TAKEAWAYS & LINKEDIN CALL TO ACTION -->
<div class="slide cover-slide" style="text-align: left; align-items: stretch; justify-content: space-between;">
  <div class="slide-header">
    <div class="brand-badge">
      <div class="brand-logo">V</div>
      <div class="brand-title">Key Learnings & Summary</div>
      <span class="vibe-tag">Portfolio Conclusion</span>
    </div>
    <div class="slide-number">Slide 09 / 09</div>
  </div>

  <div class="content-body grid-2" style="margin-top: 15px;">
    <div class="glass-card card-highlight">
      <div class="card-header">
        <div class="card-icon">🧠</div>
        <div class="card-title">Vibecoding Takeaways</div>
      </div>
      <ul class="feature-list" style="margin-bottom: 15px;">
        <li><strong>10x Development Speed:</strong> Shifted focus from writing syntax to designing system architecture & user experience.</li>
        <li><strong>High Code Quality:</strong> Leveraged strict validation with FastAPI Pydantic schemas and modular React components.</li>
        <li><strong>Seamless Polish:</strong> Built a commercial-grade Glassmorphic UI with zero compromise on visual standards.</li>
      </ul>
    </div>

    <div class="glass-card" style="justify-content: center; align-items: center; text-align: center; background: radial-gradient(circle, rgba(16, 185, 129, 0.15), transparent 70%), rgba(15, 23, 42, 0.8);">
      <div style="font-size: 40px; margin-bottom: 10px;">⭐</div>
      <h3 style="font-size: 28px; font-weight: 800; color: #F8FAFC;">Check out the Project!</h3>
      <p style="font-size: 16px; color: #94A3B8; margin-top: 10px; max-width: 500px;">
        Explore the complete open-source codebase, architecture diagrams, and documentation on GitHub.
      </p>

      <div style="margin-top: 25px; background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.15); padding: 14px 28px; border-radius: 12px; font-family: 'JetBrains Mono', monospace; font-size: 16px; color: #34D399;">
        github.com/sonnyariady/vibe-expense-tracker
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div class="footer-text"><span class="footer-dot"></span> Created with Python FastAPI, React JS & AI Vibecoding</div>
    <div class="footer-text">Thank You for Reading! • Connect on LinkedIn</div>
  </div>
</div>

</body>
</html>
"""

html_path = os.path.join(BASE_DIR, "linkedin_portfolio.html")
pdf_path = os.path.join(BASE_DIR, "VIBECODING_PORTFOLIO_LINKEDIN.pdf")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated HTML at: {html_path}")

# Run Edge headless directly to render PDF
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
cmd = [
    edge_path,
    "--headless=new",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_path}",
    f"file:///{html_path.replace(os.sep, '/')}"
]

print("Rendering PDF via Edge headless...")
res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode == 0 and os.path.exists(pdf_path):
    print(f"SUCCESS: Generated PDF at {pdf_path} (Size: {os.path.getsize(pdf_path)} bytes)")
else:
    print("FAILED to generate PDF. Error:", res.stderr)

