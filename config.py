
from crewai import LLM

MODEL_NAME = "gemini/gemini-2.5-flash"


def get_llm(gemini_api_key: str):
    """Create a Gemini LLM for CrewAI agents."""

    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY is missing.")

    return LLM(
        model=MODEL_NAME,
        api_key=gemini_api_key,
        temperature=0.3,
        max_tokens=4000,
        timeout=120,
        max_retries=2,
    )
