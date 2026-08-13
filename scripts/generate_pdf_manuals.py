import os
import re
from fpdf import FPDF
from PIL import Image

BASE_DIR = r"c:\Latihan\Fullstack\PengeluaranBulanan"

class UserManualPDF(FPDF):
    def __init__(self, title_text, lang_code="ID"):
        super().__init__()
        self.title_text = title_text
        self.lang_code = lang_code
        self.set_auto_page_break(auto=True, margin=15)

    def header(self):
        # Draw header banner on pages > 1
        if self.page_no() > 1:
            self.set_font("Helvetica", "B", 9)
            self.set_text_color(100, 100, 100)
            self.cell(0, 8, self.title_text, border=0, ln=0, align="L")
            self.set_font("Helvetica", "I", 9)
            sub_title = "Panduan Pengguna" if self.lang_code == "ID" else "User Manual"
            self.cell(0, 8, sub_title, border=0, ln=1, align="R")
            self.set_draw_color(220, 220, 220)
            self.line(10, 18, 200, 18)
            self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(128, 128, 128)
        page_str = f"Halaman {self.page_no()} dari {{nb}}" if self.lang_code == "ID" else f"Page {self.page_no()} of {{nb}}"
        self.cell(0, 10, page_str, align="C")

def sanitize_text(text):
    """Replace unsupported unicode characters for standard FPDF Helvetica font."""
    replacements = {
        "💸": "",
        "📖": "",
        "📋": "",
        "✨": "*",
        "🟢": "[SAFE]",
        "🟡": "[WARN]",
        "🔴": "[ALERT]",
        "📌": "-",
        "✓": "[x]",
        "✕": "[X]",
        "’": "'",
        "“": '"',
        "”": '"',
        "–": "-",
        "—": "-",
        "…": "...",
    }
    for orig, repl in replacements.items():
        text = text.replace(orig, repl)
    # Encode latin-1 clean
    return text.encode('latin-1', 'replace').decode('latin-1')

def markdown_to_pdf(md_filepath, output_pdf_path, title_text, lang_code="ID"):
    pdf = UserManualPDF(title_text=title_text, lang_code=lang_code)
    pdf.alias_nb_pages()
    pdf.add_page()
    
    # Cover / Header Banner
    pdf.set_fill_color(16, 185, 129) # Emerald Green
    pdf.rect(10, 10, 190, 28, style="F")
    
    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(255, 255, 255)
    pdf.set_y(15)
    pdf.cell(0, 10, sanitize_text(title_text), align="C", ln=1)
    
    pdf.set_font("Helvetica", "B", 11)
    sub = "Aplikasi Pencatatan Pengeluaran Rumah Tangga" if lang_code == "ID" else "Household Expense Tracker Web Application"
    pdf.cell(0, 6, sanitize_text(sub), align="C", ln=1)
    
    pdf.ln(12)
    pdf.set_text_color(40, 40, 40)
    
    with open(md_filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    in_code_block = False
    
    for raw_line in lines:
        line = raw_line.strip()
        
        # Skip top level duplicate title (handled by cover banner)
        if line.startswith("# ") and ("Panduan Pengguna" in line or "User Manual" in line):
            continue
        if line.startswith("## ") and ("Aplikasi Pencatatan" in line or "Household Expense" in line):
            continue
            
        if line.startswith("```"):
            in_code_block = not in_code_block
            continue
            
        if in_code_block:
            pdf.set_font("Courier", "", 9)
            pdf.set_text_color(60, 60, 60)
            pdf.multi_cell(0, 5, sanitize_text(line))
            continue
            
        # Headers
        if line.startswith("# "):
            pdf.ln(6)
            pdf.set_font("Helvetica", "B", 16)
            pdf.set_text_color(16, 185, 129)
            pdf.cell(0, 10, sanitize_text(line[2:]), ln=1)
            pdf.set_draw_color(16, 185, 129)
            pdf.line(10, pdf.get_y(), 200, pdf.get_y())
            pdf.ln(4)
        elif line.startswith("## "):
            pdf.ln(5)
            pdf.set_font("Helvetica", "B", 14)
            pdf.set_text_color(30, 41, 59)
            pdf.cell(0, 8, sanitize_text(line[3:]), ln=1)
            pdf.ln(2)
        elif line.startswith("### "):
            pdf.ln(4)
            pdf.set_font("Helvetica", "B", 11)
            pdf.set_text_color(51, 65, 85)
            pdf.cell(0, 7, sanitize_text(line[4:]), ln=1)
            pdf.ln(1)
        elif line.startswith("---"):
            pdf.ln(3)
            pdf.set_draw_color(226, 232, 240)
            pdf.line(10, pdf.get_y(), 200, pdf.get_y())
            pdf.ln(4)
        elif line.startswith("!["):
            # Image handling: ![caption](path)
            match = re.match(r"!\[(.*?)\]\((.*?)\)", line)
            if match:
                caption = match.group(1)
                rel_img_path = match.group(2)
                full_img_path = os.path.join(BASE_DIR, rel_img_path)
                
                if os.path.exists(full_img_path):
                    # Check vertical space remaining
                    if pdf.get_y() > 190:
                        pdf.add_page()
                    
                    pdf.ln(3)
                    # Add screenshot image centered
                    # A4 width = 210mm, margin = 10mm each side, printable = 190mm
                    img_width = 175
                    pdf.image(full_img_path, x=17.5, w=img_width)
                    pdf.ln(2)
                    
                    # Caption
                    pdf.set_font("Helvetica", "I", 8)
                    pdf.set_text_color(100, 116, 139)
                    pdf.cell(0, 5, sanitize_text(f"Gambar: {caption}"), align="C", ln=1)
                    pdf.ln(4)
                    pdf.set_text_color(40, 40, 40)
        elif line.startswith("> "):
            # Callout quote
            pdf.set_fill_color(241, 245, 249)
            pdf.set_font("Helvetica", "I", 9.5)
            pdf.set_text_color(51, 65, 85)
            clean_quote = line[2:].replace("[!TIP]", "TIPS:").replace("[!IMPORTANT]", "IMPORTANT:")
            pdf.multi_cell(0, 6, sanitize_text(clean_quote), fill=True)
            pdf.ln(2)
        elif line.startswith("* ") or line.startswith("- "):
            pdf.set_font("Helvetica", "", 10)
            pdf.set_text_color(40, 40, 40)
            bullet_text = sanitize_text(line[2:])
            # bold formatting like **Text**:
            pdf.multi_cell(0, 5, f"  * {bullet_text}")
            pdf.ln(1)
        elif re.match(r"^\d+\.", line):
            pdf.set_font("Helvetica", "", 10)
            pdf.set_text_color(40, 40, 40)
            pdf.multi_cell(0, 5, sanitize_text(line))
            pdf.ln(1)
        elif line == "":
            pdf.ln(2)
        else:
            pdf.set_font("Helvetica", "", 10)
            pdf.set_text_color(40, 40, 40)
            # Remove bold markdown tags for clean pdf
            clean_p = line.replace("**", "")
            pdf.multi_cell(0, 5.5, sanitize_text(clean_p))
            pdf.ln(2)
            
    pdf.output(output_pdf_path)
    print(f"Successfully generated PDF: {output_pdf_path}")

def main():
    id_md = os.path.join(BASE_DIR, "USER_MANUAL_ID.md")
    id_pdf = os.path.join(BASE_DIR, "USER_MANUAL_ID.pdf")
    markdown_to_pdf(id_md, id_pdf, "Panduan Pengguna Household Expense Tracker", lang_code="ID")

    en_md = os.path.join(BASE_DIR, "USER_MANUAL_EN.md")
    en_pdf = os.path.join(BASE_DIR, "USER_MANUAL_EN.pdf")
    markdown_to_pdf(en_md, en_pdf, "Household Expense Tracker User Manual", lang_code="EN")

if __name__ == "__main__":
    main()
