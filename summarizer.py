from transformers import pipeline
import textwrap

# Load the summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text):
    max_chunk_size = 1000
    chunks = textwrap.wrap(text, max_chunk_size)

    summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
        summaries.append(summary)

    return "\n\n".join(summaries)

def extract_key_points(summary_text):
    prompt = (
        "Extract the 3 to 5 most important key points or highlights from this summary:\n\n"
        f"{summary_text}\n\n"
        "Return them as bullet points."
    )

    result = summarizer(prompt, max_length=100, min_length=30, do_sample=False)
    return result[0]['summary_text']

def generate_citation(summary_text, style="APA"):
    if style.upper() == "APA":
        prompt = (
            "Based on the following research paper summary, generate an APA-style citation:\n\n"
            f"{summary_text}"
        )
    else:
        prompt = (
            "Based on the following research paper summary, generate an MLA-style citation:\n\n"
            f"{summary_text}"
        )

    result = summarizer(prompt, max_length=60, min_length=20, do_sample=False)
    return result[0]['summary_text']

