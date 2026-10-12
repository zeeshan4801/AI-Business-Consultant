
from crewai import Agent


def create_analysis_agent(llm):
    return Agent(
        role="Senior Business Analyst",

        goal=(
            "Analyze business strengths, weaknesses, "
            "opportunities, threats, competition, "
            "business economics, and strategic risks."
        ),

        backstory=(
            "You are an analytical consultant who "
            "specializes in SWOT analysis, business "
            "models, competitive positioning, and "
            "decision-making under uncertainty."
        ),

        llm=llm,
        verbose=False,
        allow_delegation=False,
        max_iter=3,
    )
