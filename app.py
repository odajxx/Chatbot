# AIzaSyACpXKcfK_s1lfMQYO5CKgfDsFkeh1ApjA

import streamlit as st
from google import genai
from google.genai import types
from datetime import datetime

st.title("AI Chatbot - Based on Gemini")

with st.sidebar:
    st.header("Configs")

    api_key = st.text_input("Enter your API Key", type="password")

    model_name = st.selectbox(
        "Select Model:",
        ["gemini-2.5-flash", "gemini-2.5-pro"]
    )

if "messages" not in st.session_state: # Message history. using a datbase is better and more realistic
    st.session_state.messages = []

if prompt := st.chat_input("Ask me something"):
    # pass
    if not api_key:
        st.error("Please enter API key")
        st.stop()

timestamp = datetime.now().strftime("%Y-%M-%D :: %H:%M:%S")

st.session_state.messages.append(
    {
        "role": "user",
        "content": prompt,
        "timestamp": timestamp
    }
)

with st.chat_messages("user"):
    st.markdown(prompt)
    st.caption(f"{timestamp}")