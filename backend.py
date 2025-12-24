# backend.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from ai_agent import get_response_from_ai_agent

app = FastAPI(title="LangGraph AI Agent")


class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool


ALLOWED_MODELS_NAMES = [
    "llama-3.3-70b-versatile",
    "mixtral-8x7b-32768",
    "gpt-4o-mini"
]


@app.post("/chat")
def chat_endpoint(request: RequestState):

    if request.model_name not in ALLOWED_MODELS_NAMES:
        return {"error": "Model not allowed"}

    provider = request.model_provider.strip().lower()

    if provider not in ["groq", "openai"]:
        return {"error": "Invalid model provider"}

    query = " ".join(request.messages)

    response = get_response_from_ai_agent(
        llm_id=request.model_name,
        query=query,
        allow_search=request.allow_search,
        system_prompt=request.system_prompt or "You are a helpful AI assistant.",
        provider=provider
    )

    return {"response": response}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
