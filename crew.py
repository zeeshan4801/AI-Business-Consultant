
from crewai import Crew, Task, Process

from agents.research_agent import create_research_agent
from agents.analysis_agent import create_analysis_agent
from agents.strategy_agent import create_strategy_agent

from tools.news_research import get_market_news


def generate_business_report(
    business_name,
    industry,
    location,
    target_customers,
    business_goal,
    additional_details,
    llm,
):
    # STEP 1: Create the three agents
    researcher = create_research_agent(llm)
    analyst = create_analysis_agent(llm)
    strategist = create_strategy_agent(llm)

    # STEP 2: Gather external research leads
    news = get_market_news(industry, location)

    business_info = f"""
    Business Name: {business_name}
    Industry: {industry}
    Location: {location}
    Target Customers: {target_customers}
    Main Business Goal: {business_goal}
    Additional Details: {additional_details}
    """

    # STEP 3: Define research task
    research_task = Task(
        description=f"""
        Research the following business:

        {business_info}

        Available recent news leads:
        {news}

        Evaluate:
        1. Industry environment
        2. Target customers
        3. Market trends
        4. Competitor categories
        5. Potential opportunities

        Cite URLs for claims supported by news.
        News headlines are not fully verified articles.
        Do not invent competitors, revenues, statistics,
        sources, or market-share figures.

        Clearly identify unknown information.
        """,
        expected_output=(
            "A market research briefing with "
            "source links, observations, assumptions, "
            "and research limitations."
        ),
        agent=researcher,
    )

    # STEP 4: Define analysis task
    analysis_task = Task(
        description=f"""
        Analyze this business:

        {business_info}

        Use the research report to develop:
        1. SWOT analysis
        2. Competitive positioning
        3. Business model evaluation
        4. Major risks
        5. Key opportunities
        6. Financial considerations

        Use qualitative analysis where reliable
        numerical data is unavailable.
        Do not fabricate financial projections.
        """,
        expected_output=(
            "A detailed business analysis "
            "including SWOT, risks, opportunities, "
            "and evidence-based conclusions."
        ),
        agent=analyst,
        context=[research_task],
    )

    # STEP 5: Define final strategy task
    strategy_task = Task(
        description=f"""
        Create a professional strategy report
        for this business:

        {business_info}

        Use the research and business analysis.

        Include these Markdown sections:

        # Business Strategy Report
        ## Executive Summary
        ## Market Research
        ## Customer Segmentation
        ## Competitive Analysis
        ## SWOT Analysis
        ## Strategic Recommendations
        ## Marketing and Sales Strategy
        ## Financial Considerations
        ## 30/60/90-Day Action Plan
        ## Key Performance Indicators
        ## Major Risks
        ## Evidence and Limitations

        Make recommendations practical,
        prioritized, and specific.

        Every proposed financial metric without
        real input data must be labeled as an
        assumption or illustrative scenario.

        Clearly distinguish verified evidence
        from strategic interpretation.
        """,
        expected_output=(
            "A complete professional business "
            "strategy report in Markdown format."
        ),
        agent=strategist,
        context=[research_task, analysis_task],
    )

    # STEP 6: Build the CrewAI team
    consulting_crew = Crew(
        agents=[
            researcher,
            analyst,
            strategist,
        ],
        tasks=[
            research_task,
            analysis_task,
            strategy_task,
        ],
        process=Process.sequential,
        verbose=False,
        memory=False,
    )

    # STEP 7: Execute all three agents
    result = consulting_crew.kickoff()

    return str(result)
