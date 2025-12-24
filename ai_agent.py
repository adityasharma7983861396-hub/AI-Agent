# ai_agent.py
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, SystemMessage


def get_response_from_ai_agent(
    llm_id: str,
    query: str,
    allow_search: bool,
    system_prompt: str,
    provider: str
):

    # ---- Select LLM ----
    if provider == "groq":
        llm = ChatGroq(model=llm_id)
    elif provider == "openai":
        llm = ChatOpenAI(model=llm_id)
    else:
        raise ValueError("Invalid provider")

    # ---- Tools ----
    tools = [TavilySearch(max_results=3)] if allow_search else []

    # ---- With tools (ReAct agent) ----
    if tools:
        agent = create_react_agent(llm, tools)

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=query)
        ]

        result = agent.invoke({"messages": messages})
        return result["messages"][-1].content

    # ---- Without tools (Direct LLM) ----
    else:
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=query)
        ]
        return llm.invoke(messages).content
