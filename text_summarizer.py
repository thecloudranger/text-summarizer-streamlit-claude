import streamlit as st
from anthropic import Anthropic
import os

# Initialize the Anthropic client
anthropic = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

st.title('Text Summarizer')

def summarize_text(text):
    prompt = f"\n\nHuman: Please summarize the following text concisely:\n\n{text}\n\nAssistant:"
    response = anthropic.completions.create(
        model="claude-2.1",
        prompt=prompt,
        max_tokens_to_sample=150,
        temperature=0.5
    )
    return response.completion

# Text input area
input_text = st.text_area("Enter the text you want to summarize:", height=200)

if st.button('Summarize'):
    if input_text:
        summary = summarize_text(input_text)
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.warning("Please enter some text to summarize.")
