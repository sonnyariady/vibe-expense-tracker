import os
import time
from playwright.sync_api import sync_playwright

OUTPUT_DIR = r"c:\Latihan\Fullstack\PengeluaranBulanan\docs\screenshots"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def capture_all():
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True)
        except Exception:
            browser = p.chromium.launch(channel="msedge", headless=True)
            
        context = browser.new_context(viewport={"width": 1280, "height": 800}, device_scale_factor=2)
        page = context.new_page()

        print("Navigating to http://localhost:3000...")
        page.goto("http://localhost:3000", wait_until="networkidle")
        time.sleep(1)

        # 1. Full Header Period Navigation
        print("Capturing 01_header_period_navigation.png...")
        page.screenshot(path=os.path.join(OUTPUT_DIR, "01_header_period_navigation.png"))

        # 2. KPI Summary Cards
        print("Capturing 02_kpi_dashboard.png...")
        kpi_section = page.locator(".stats-grid, .grid, header + div").first
        if kpi_section.is_visible():
            kpi_section.screenshot(path=os.path.join(OUTPUT_DIR, "02_kpi_dashboard.png"))
        else:
            page.screenshot(path=os.path.join(OUTPUT_DIR, "02_kpi_dashboard.png"))

        # 3. Visual Analytics (Charts)
        print("Capturing 03_visual_analytics.png...")
        page.evaluate("window.scrollTo(0, 250)")
        time.sleep(0.5)
        page.screenshot(path=os.path.join(OUTPUT_DIR, "03_visual_analytics.png"))

        # 4. Add Expense Form Modal
        print("Opening modal and capturing 04_add_expense_modal.png...")
        page.evaluate("window.scrollTo(0, 0)")
        time.sleep(0.5)
        
        # Click "+ Tambah Pengeluaran" button
        add_btn = page.locator("button:has-text('Tambah Pengeluaran')").first
        if add_btn.is_visible():
            add_btn.click()
            time.sleep(0.5)

            # Fill in modal fields using placeholders & tag types
            title_input = page.locator("input[placeholder*='Belanja Sayuran']")
            if title_input.is_visible():
                title_input.fill("Belanja Sembako Mingguan")
            
            amount_input = page.locator("input[placeholder='0']")
            if amount_input.is_visible():
                amount_input.fill("350000")
            
            notes_input = page.locator("textarea")
            if notes_input.is_visible():
                notes_input.fill("Beli Beras 10kg, Minyak Goreng 2L, Daging Sapi, & Telur Ayam")

            time.sleep(0.5)
            page.screenshot(path=os.path.join(OUTPUT_DIR, "04_add_expense_modal.png"))

            # Close modal using button
            close_btn = page.locator("button:has-text('Batal')").first
            if close_btn.is_visible():
                close_btn.click()
            else:
                page.keyboard.press("Escape")
            time.sleep(0.5)

        # 5. Filters and Search
        print("Capturing 05_filters_and_search.png...")
        page.evaluate("window.scrollTo(0, 450)")
        time.sleep(0.5)
        search_input = page.locator("input[placeholder*='Cari']")
        if search_input.count() > 0 and search_input.first.is_visible():
            search_input.first.fill("Beras")
            time.sleep(0.5)
            page.screenshot(path=os.path.join(OUTPUT_DIR, "05_filters_and_search.png"))
            search_input.first.fill("")
            time.sleep(0.5)
        else:
            page.screenshot(path=os.path.join(OUTPUT_DIR, "05_filters_and_search.png"))

        # 6. Action buttons (Edit/Delete) in Table
        print("Capturing 06_action_edit_delete.png...")
        page.evaluate("window.scrollTo(0, 550)")
        time.sleep(0.5)
        page.screenshot(path=os.path.join(OUTPUT_DIR, "06_action_edit_delete.png"))

        # 7. CSV Export Button highlight
        print("Capturing 07_export_csv.png...")
        page.evaluate("window.scrollTo(0, 0)")
        time.sleep(0.5)
        export_btn = page.locator("button:has-text('Export CSV')").first
        if export_btn.is_visible():
            export_btn.hover()
            time.sleep(0.3)
        page.screenshot(path=os.path.join(OUTPUT_DIR, "07_export_csv.png"))

        browser.close()
        print("All screenshots successfully captured!")

if __name__ == "__main__":
    capture_all()
