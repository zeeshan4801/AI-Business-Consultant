
# AI Business Consulting Team

A beginner-friendly, multi-agent business consulting
application built with CrewAI, Groq, and Streamlit.

## Features

- AI-powered market research
- SWOT analysis
- Competitor and customer analysis
- Strategic business recommendations
- 30/60/90-day implementation roadmap
- Downloadable Markdown business strategy report

## AI Agents

1. Market Research Specialist
2. Business Analyst
3. Business Strategy Consultant

All agents use Groq's GPT-OSS 120B model.

## Technology

- Python
- CrewAI
- Groq API
- Streamlit
- Python standard library for RSS retrieval

## Deployment

1. Upload project files to GitHub.
2. Open https://share.streamlit.io
3. Sign in using GitHub.
4. Select this repository.
5. Set main file to app.py.
6. Choose Python 3.12.
7. Add GROQ_API_KEY in Streamlit Secrets.
8. Click Deploy.

## Streamlit Secret

GROQ_API_KEY = "your_actual_groq_api_key"

Never upload a real API key to GitHub.

## Running the Application

Open the deployed Streamlit URL.

Enter:
- Business name
- Industry
- Location
- Target customers
- Main business goal
- Additional details

Click Generate Business Strategy.

## Limitations

The MVP uses business details and public RSS news
headlines, not comprehensive verified market research.

Financial calculations and company-specific statistics
must be independently validated.

News retrieval depends on external RSS availability.
The agent reports this limitation when retrieval fails.
