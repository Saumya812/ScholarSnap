import streamlit as st
from ocr_utils import extract_text_from_image, extract_text_from_pdf
from summarizer import generate_summary, extract_key_points, generate_citation
from pdf_utils import generate_pdf
import base64  # only need to import once

# 🔽 DOWNLOAD BUTTON FUNCTION
def create_download_button(summary_text):
    b64 = base64.b64encode(summary_text.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="summary.txt">📥 Download Summary</a>'
    st.markdown(href, unsafe_allow_html=True)

# 🔽 MAIN UI
st.title("📚 ScholarSnap — AI-powered Paper Summarizer")

uploaded_file = st.file_uploader("Upload an image or PDF of a research paper", type=["png", "jpg", "jpeg", "pdf"])

if uploaded_file is not None:
    # Extract text based on file type
    if uploaded_file.type == "application/pdf":
        extracted_text = extract_text_from_pdf(uploaded_file)
    else:
        extracted_text = extract_text_from_image(uploaded_file)

    st.subheader("📄 Extracted Text:")
    st.write(extracted_text)

    if extracted_text.strip():
        summary = generate_summary(extracted_text)

        st.subheader("🧠 Summary:")
        st.write(summary)

        # ✅ Only show download if there's a summary
        create_download_button(summary)

        # ✅ KEY HIGHLIGHTS BUTTON
        if st.button("🔍 Highlight Important Info"):
            with st.spinner("Extracting key points..."):
                key_points = extract_key_points(summary)
                st.subheader("⭐ Key Highlights:")
                st.markdown("- " + "\n- ".join(key_points.split('\n')))

        # ✅ CITATION GENERATOR
        st.subheader("📚 Generate Citation")
        style = st.selectbox("Choose citation style", ["APA", "MLA"])
        if st.button("📎 Generate Citation"):
            with st.spinner("Generating citation..."):
                citation = generate_citation(summary, style=style)
                st.code(citation, language='markdown')

        # ✅ PDF EXPORT
        st.subheader("📄 Download PDF Report")

        include_summary = st.checkbox("Include Summary", value=True)
        include_highlights = st.checkbox("Include Highlights")
        include_citation = st.checkbox("Include Citation")
        include_extracted = st.checkbox("Include Extracted Text")

        if st.button("📥 Download PDF"):
            hl = extract_key_points(summary) if include_highlights else None
            cite = generate_citation(summary, style) if include_citation else None
            extracted = extracted_text if include_extracted else None

            pdf_path = generate_pdf(
                summary if include_summary else None,
                highlights=hl,
                citation=cite,
                extracted_text=extracted
            )

            with open(pdf_path, "rb") as f:
                st.download_button(
                    label="📥 Click here to download your PDF",
                    data=f,
                    file_name="ScholarSnap_Summary.pdf",
                    mime="application/pdf"
                )


