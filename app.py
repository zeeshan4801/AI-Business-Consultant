
import os
import streamlit as st

from config import get_llm
from crew import generate_business_report


st.set_page_config(
    page_title="AI Business Consultant",
    page_icon="📊",
    layout="wide",
)

st.title("📊 AI Business Consulting Team")

st.write(
    "Generate professional business strategies "
    "using three specialized AI agents powered "
    "by CrewAI and Groq."
)

# Read the API key securely
try:
    groq_api_key = st.secrets.get("GROQ_API_KEY", "")
except Exception:
    groq_api_key = ""

# Optional support for environment variables
if not groq_api_key:
    groq_api_key = os.getenv("GROQ_API_KEY", "")

if not groq_api_key:
    st.error(
        "GROQ_API_KEY is not configured. "
        "Add it in Streamlit App Settings > Secrets."
    )
    st.stop()

st.subheader("Enter Business Information")

with st.form("business_form"):

    business_name = st.text_input(
        "Business Name",
        placeholder="Example: Smart Fashion Store",
    )

    industry = st.text_input(
        "Industry",
        placeholder="Example: Fashion Retail",
    )

    location = st.text_input(
        "Target Market / Location",
        placeholder="Example: Lahore, Pakistan",
    )

    target_customers = st.text_input(
        "Target Customers",
        placeholder="Example: Women aged 18-35",
    )

    business_goal = st.selectbox(
        "Main Business Goal",
        [
            "Start a new business",
            "Increase sales",
            "Expand into new markets",
            "Improve profitability",
            "Improve marketing strategy",
            "Analyze competitors",
        ],
    )

    additional_details = st.text_area(
        "Additional Business Details",
        placeholder=(
            "Describe products, budget, "
            "current sales, challenges, "
            "or anything else relevant."
        ),
        height=130,
    )

    submitted = st.form_submit_button(
        "🚀 Generate Business Strategy",
        type="primary",
        use_container_width=True,
    )


if submitted:

    if not business_name.strip() or not industry.strip():
        st.warning(
            "Please provide a business name and industry."
        )

    else:
        try:
            llm = get_llm(groq_api_key)

            with st.spinner(
                "Your AI consulting team is analyzing "
                "the business..."
            ):

                report = generate_business_report(
                    business_name=business_name,
                    industry=industry,
                    location=location or "Not specified",
                    target_customers=(
                        target_customers or "Not specified"
                    ),
                    business_goal=business_goal,
                    additional_details=additional_details,
                    llm=llm,
                )

            st.session_state["report"] = report
            st.session_state["report_business"] = business_name

            st.success(
                "Business strategy report generated!"
            )

        except Exception as exc:
            st.error("Report generation failed.")
            st.error(str(exc))

            st.info(
                "Check your Groq API key, model access, "
                "and Groq rate limits. "
                "For installation errors, inspect "
                "the Streamlit Cloud logs."
            )


if "report" in st.session_state:

    st.divider()
    st.subheader("📋 Your Business Strategy Report")

    st.markdown(st.session_state["report"])

    st.download_button(
        label="📥 Download Report",
        data=st.session_state["report"],
        file_name="business_strategy_report.md",
        mime="text/markdown",
        use_container_width=True,
    )
