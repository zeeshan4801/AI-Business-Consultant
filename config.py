
from crewai import LLM

MODEL_NAME = "gemini/gemini-3.8-flash"


def get_llm(gemini_api_key: str):
    """Create Gemini LLM for CrewAI."""

    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY is missing.")

    return LLM(
        model=MODEL_NAME,
        api_key=gemini_api_key,
        max_tokens=4000,
        timeout=120,
        max_retries=2,
    )
