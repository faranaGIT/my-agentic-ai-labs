import streamlit as st
import requests

st.title("Groq ChatBot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
       st.markdown(msg["content"])

# Chat Input
if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking...."):
            response = requests.post("http://localhost:8000/generate",
                                     json={"message": prompt})
            result = response.json()
            st.markdown(result["message"])
    st.session_state.messages.append(
        {"role": "assistant", "content": result["message"]})
