import streamlit as st
from transformers import pipeline

# Load the sentiment-analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# App title
st.set_page_config(page_title="AI Sentiment Analyzer", layout="centered")
st.title("🧠 AI-Powered Sentiment Analyzer")

# Instructions
st.markdown("Type or paste some text below to find out the sentiment! 📊")

# Text input
user_input = st.text_area("Enter your text here:", height=150)

# Analyze button
if st.button("🔍 Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        result = sentiment_pipeline(user_input)[0]
        label = result['label']
        score = result['score']

        # Display result with emoji
        sentiment_emoji = {
            "POSITIVE": "😊",
            "NEGATIVE": "😠",
            "NEUTRAL": "😐"  # Some models may return this
        }

        # Prepare downloadable results
        result_text = (
            f"Sentiment Analysis Result\n"
            f"-------------------------\n"
            f"Text: {user_input}\n\n"
            f"Sentiment: {label}\n"
            f"Confidence Score: {score:.2f}\n"
        )

        # Add a download button
        st.download_button(
            label="📄 Download Result as .txt",
            data=result_text,
            file_name="sentiment_analysis.txt",
            mime="text/plain"
        )

        emoji = sentiment_emoji.get(label, "🤖")

        st.markdown("---")
        st.subheader("Result")
        st.write(f"**Sentiment:** {label} {emoji}")
        st.write(f"**Confidence Score:** {score:.2f}")
