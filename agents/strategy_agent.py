
from crewai import Agent


def create_strategy_agent(llm):
    return Agent(
        role="Lead Business Strategy Consultant",

        goal=(
            "Develop practical business strategies "
            "using the research and analysis provided."
        ),

        backstory=(
            "You are a strategic business consultant "
            "who turns research into actionable "
            "recommendations, implementation roadmaps, "
            "and measurable business objectives."
        ),

        llm=llm,
        verbose=False,
        allow_delegation=False,
        max_iter=3,
    )
