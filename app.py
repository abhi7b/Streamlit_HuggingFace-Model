import torch
import streamlit as st
from transformers import pipeline

# --- Set Page Configuration ---
st.set_page_config(page_title="Document Summarizer", page_icon="📝", layout="centered")

# --- Custom CSS for a Futuristic Dark Theme with Neon Accents ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');

body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    font-family: 'Orbitron', sans-serif;
    margin: 0;
    padding: 0;
    color: #ecf0f1;
}

.main-container {
    background: rgba(20, 20, 20, 0.85);
    padding: 2rem 3rem;
    border-radius: 12px;
    margin: 3rem auto;
    max-width: 800px;
    border: 1px solid #1abc9c;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
}

.header {
    text-align: center;
    font-size: 2.8rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
    color: #1abc9c;
    text-shadow: 0 0 10px #1abc9c;
}

.subheader {
    text-align: center;
    font-size: 1.2rem;
    margin-bottom: 2rem;
    color: #bdc3c7;
}

textarea {
    width: 100%;
    padding: 1rem;
    border-radius: 8px;
    border: 2px solid #1abc9c;
    margin-top: 1rem;
    font-size: 1rem;
    resize: vertical;
    background: rgba(30, 30, 30, 0.9);
    color: #ecf0f1;
}

/* Style the default Streamlit button */
div.stButton > button {
    background-color: #1abc9c !important;
    color: #0f2027 !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.75rem 1.5rem !important;
    font-size: 1.1rem !important;
    cursor: pointer !important;
    transition: background-color 0.3s ease, transform 0.3s ease !important;
    width: 100%;
}

div.stButton > button:hover {
    background-color: #16a085 !important;
    transform: scale(1.02) !important;
}

.summary-output {
    background: rgba(30, 30, 30, 0.9);
    border-radius: 8px;
    padding: 1.5rem;
    margin-top: 2rem;
    font-size: 1.2rem;
    color: #ecf0f1;
    border: 1px solid #1abc9c;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

# --- Load the Summarization Model using st.cache_resource ---
@st.cache_resource
def load_summarization_model():
    return pipeline("summarization", model="facebook/bart-large-cnn", device=-1)

sum_model = load_summarization_model()

# --- Main Container ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<div class="header">Document Summarizer</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Paste your text below to generate a summary.</div>', unsafe_allow_html=True)

# --- Text Area for Input (with simplified label) ---
text_input = st.text_area("Paste your text:", height=200, help="Enter the text to be summarized.")

# --- Summarize Button and Processing ---
if st.button("Summarize", key="summarize_btn", help="Click to summarize your text"):
    if text_input.strip() == "":
        st.warning("Please paste your text for summarization.")
    else:
        with st.spinner("Summarizing..."):
            summary = sum_model(text_input, max_new_tokens=150, min_length=30, do_sample=False)
            summary_text = summary[0]['summary_text']
        st.markdown(f'<div class="summary-output"><strong>Summary:</strong><br>{summary_text}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
