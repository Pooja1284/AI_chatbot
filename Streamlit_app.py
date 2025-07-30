import streamlit as st
import google.generativeai as genai

st.title("Free Chatbot using Gemini (by Google)")

# 🔐 Paste your Gemini API key here
genai.configure(api_key="AIzaSyAeG9w6uCOg_MsyaRM1_Y9IuOoNqOGFEGQ")

# Initialize Gemini model
model = genai.GenerativeModel("models/gemini-2.5-flash")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Handle new input
if prompt := st.chat_input("Ask me anything..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = model.generate_content(prompt)
                reply = response.text
            except Exception as e:
                reply = f"Error: {e}"

            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
