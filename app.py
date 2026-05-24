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

    with st.chat_message("user"):
        st.markdown(prompt)
        st.caption(f"{timestamp}")

    with st.chat_message("chatbot"):
        try:
            contents = []
            for msg in st.session_state.messages:
                role = "model" if msg["role"] == "chatbot" else "user"
                contents.append(
                    {
                        "role": role,
                        "parts": [{"text": msg["content"]}]
                    }
                )

            client = genai.Client(api_key=api_key)

            response_stream = client.models.generate_content_stream(
                model=model_name,
                contents=contents
            )

            response_pleaceholder = st_empty()
            full_response = " "

            for chunk in response_stream:
                if hassttr(shunk, "text") and chunk.text:
                    response_placeholder.markdown(full_response + "|")

            response_placeholder.markdown(full_response)
            response_timpstamp = datetime.now().strftime("%Y-%M-%D :: %H:%M:%S")
            st.caption(f"*{response_timestamp}")

            st.session_state.messages.append(
                {
                    "role": "chatbot",
                    "content": full_response,
                    "timestamp": timestamp
                }
            )
        except Exception as e:
            st.error(f"Error {str(e)}")