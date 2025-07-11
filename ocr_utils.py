import pytesseract
from PIL import Image
import io
import fitz  # PyMuPDF

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(uploaded_file):
    image = Image.open(io.BytesIO(uploaded_file.read()))
    text = pytesseract.image_to_string(image)
    return text

def extract_text_from_pdf(uploaded_file):
    pdf_text = ""
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    for page in doc:
        pdf_text += page.get_text()
    return pdf_text

