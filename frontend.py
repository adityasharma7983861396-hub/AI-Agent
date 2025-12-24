# frontend.py
import streamlit as st
import requests

st.set_page_config(page_title="LangGraph Agent UI", layout="centered")
st.title("AI Chatbot Agents")
st.write("Create and Interact with AI Agents")

system_prompt = st.text_area(
    "Define your AI Agent:",
    placeholder="You are a helpful AI assistant...",
    height=80
)

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

model_provider = st.selectbox("Model Provider", ["Groq", "OpenAi"])

if model_provider == "Groq":
    selected_model = st.selectbox("Select Model", MODEL_NAMES_GROQ)
else:
    selected_model = st.selectbox("Select Model", MODEL_NAMES_OPENAI)

allow_web_search = st.checkbox("Allow Web Search")

user_query = st.text_area(
    "Enter your query:",
    height=150,
    placeholder="Ask anything..."
)

API_URL = "http://127.0.0.1:8000/chat"

if st.button("Ask Agent"):
    if not user_query.strip():
        st.warning("Please enter a query.")
    else:
        payload = {
            "model_name": selected_model,
            "model_provider": model_provider.lower(),  # 🔥 FIX
            "system_prompt": system_prompt,
            "messages": [user_query],  # 🔥 FIX
            "allow_search": allow_web_search
        }

        try:
            response = requests.post(API_URL, json=payload)

            if response.status_code == 200:
                data = response.json()
                if "error" in data:
                    st.error(data["error"])
                else:
                    st.subheader("Agent Response")
                    st.markdown(data["response"])
            else:
                st.error(f"Server error: {response.status_code}")

        except requests.exceptions.ConnectionError:
            st.error("Backend server not running. Start backend.py")
