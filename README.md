AI Agent – LangGraph Based Chatbot

An end-to-end AI chatbot agent built using LangGraph and LangChain, supporting multiple LLM providers such as Groq and OpenAI, with an optional web search feature powered by Tavily.
The project includes a FastAPI backend and a Streamlit frontend, providing a clean and interactive user experience.


Features:

🔹 ReAct-based AI Agent (Reasoning + Acting)

🔹 Multi-LLM support (Groq & OpenAI)

🔹 Optional real-time web search using Tavily

🔹 Custom system prompt support

🔹 FastAPI backend for scalable API access

🔹 Streamlit-based interactive UI

🔹 Clean and modular project structure

🔹 Secure environment variable handling

Architecture Overview

  1. Frontend (Streamlit)
  
      User interface to select model, provider, system prompt, and send queries.

  2. Backend (FastAPI)
  
      Handles API requests, validates input, and communicates with the AI agent.

  3. AI Agent (LangGraph + LangChain)
  
      Uses a ReAct agent that can reason step-by-step and optionally call tools like web search.

Tech Stack

  1. Python

  2. LangChain

  3. LangGraph

  4. Groq API

  5. OpenAI API

  6. Tavily Search

  7. FastAPI

  8. Streamlit




  
