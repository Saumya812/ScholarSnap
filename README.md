# ScholarSnap – The Smart Academic Note Reader

ScholarSnap is an AI-powered tool that helps students transform handwritten notes, scanned PDFs, and textbooks into clean, searchable, and interactive study material. Say goodbye to messy raw text and hello to structured summaries, intelligent tagging, and instant Q&A — all powered by cutting-edge AI.

## Problem

Students often rely on handwritten notes or scanned materials, but:

- They forget what's inside them.  
- Searching through messy handwriting or scanned files is frustrating.  
- Extracted text is unstructured and difficult to use.  
- Summarizing or understanding key concepts takes time and effort.  

## Solution

ScholarSnap combines **OCR** and **AI/NLP** to offer a smarter study experience:

- Converts scanned or handwritten content into structured, clean digital notes.  
- Detects key topics and auto-generates helpful tags.  
- Summarizes entire chapters or sections into digestible points.  
- Lets you ask questions about your notes — ChatGPT-style Q&A from your own content.  

## Tech Stack

| Layer           | Technologies Used                                         | Notes                                      |
|-----------------|----------------------------------------------------------|--------------------------------------------|
| Frontend/UI     | Streamlit                                                | Interactive web-based user interface       |
| Backend Logic   | Python                                                   | Core logic for OCR, NLP, and UI integration|
| AI/NLP          | Transformers (facebook/bart-large-cnn)                   | Summarization, citation extraction, tagging|
| OCR             | pytesseract, PyMuPDF (fitz)                              | Text extraction from images and PDFs       |
| PDF Export      | fpdf                                                     | Generates structured, downloadable PDFs    |
| File Handling   | base64, Streamlit uploader                               | Upload, process, and download support      |
| Deployment      | *(Planned)* Streamlit Cloud / Hugging Face Spaces       | Free and fast ML web app hosting platforms |

## How It Works

1. Upload a handwritten note, scanned image, or PDF file.  
2. The app uses OCR to extract raw text from the input.  
3. NLP modules process the content to detect topics, generate tags, and summarize.  
4. Interact with your notes via a chatbot-style Q&A interface.  

## Use Cases

- Study smarter with AI-generated summaries and key points.  
- Convert handwritten class notes into clean digital notes.  
- Search and explore large scanned documents easily.  
- Get instant answers to questions based on your notes.  

## Author

Saumya Brahmbhatt  
Computer Science Major  
LinkedIn:(https://www.linkedin.com/in/saumyabrahmbhatt/)  
Email: saumyabrahmbhatt812@gmail.com  

## Acknowledgments

This project was fully conceptualized and developed by me as an original idea.  
Special thanks to Harford Community College for supporting my academic journey and growth in computer science.
