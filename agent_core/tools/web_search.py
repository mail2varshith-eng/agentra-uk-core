def mock_web_search(query: str) -> str:
    """
    Mock web search instead of calling real APIs.
    This keeps the MVP simple and runnable anywhere.

    In a later version, this can be replaced with:
    - Real web search
    - API queries
    - Vector search, etc.
    """

    base_info = {
        "LangChain": "LangChain – framework for building LLM-powered applications and agents.",
        "AutoGPT": "AutoGPT – experimental open-source agent that autonomously runs tasks using LLMs.",
        "CrewAI": "CrewAI – multi-agent orchestration framework for collaborative agents.",
    }

    joined = "\n".join([f"{name}: {desc}" for name, desc in base_info.items()])
    return f"Mock search results for: {query}\n\n{joined}"
