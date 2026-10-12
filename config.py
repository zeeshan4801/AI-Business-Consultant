
from crewai import LLM

MODEL_NAME = "groq/openai/gpt-oss-120b"


def get_llm(groq_api_key: str):
    """Create a CrewAI LLM powered by Groq."""

    if not groq_api_key:
        raise ValueError("GROQ_API_KEY is missing.")

    return LLM(
        model=MODEL_NAME,
        api_key=groq_api_key,
        max_tokens=4000,
        timeout=120,
        max_retries=2,
    )
