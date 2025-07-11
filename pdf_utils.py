from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "📚 ScholarSnap Summary", ln=True, align="C")
        self.ln(10)

    def section_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.ln(4)

    def section_body(self, body):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 10, body)
        self.ln()

def generate_pdf(summary, highlights=None, citation=None, extracted_text=None):
    pdf = PDF()
    pdf.add_page()

    if summary:
        pdf.section_title("🧠 Summary")
        pdf.section_body(summary)

    if highlights:
        pdf.section_title("⭐ Key Highlights")
        pdf.section_body(highlights)

    if citation:
        pdf.section_title("📎 Citation")
        pdf.section_body(citation)

    if extracted_text:
        pdf.section_title("📄 Extracted Text")
        pdf.section_body(extracted_text)

    output_path = "summary_output.pdf"
    pdf.output(output_path)
    return output_path
