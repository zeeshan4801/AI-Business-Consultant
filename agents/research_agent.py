
from crewai import Agent


def create_research_agent(llm):
    return Agent(
        role="Senior Market Research Specialist",

        goal=(
            "Research the company's market, customers, "
            "competitors, industry trends, and opportunities."
        ),

        backstory=(
            "You are an experienced business researcher. "
            "You distinguish evidence from assumptions "
            "and never invent statistics or sources."
        ),

        llm=llm,
        verbose=False,
        allow_delegation=False,
        max_iter=3,
    )
