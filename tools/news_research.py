
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET


def get_market_news(industry, location, limit=6):
    """Fetch relevant current news via public RSS."""

    search_terms = f"{industry} {location} business market"

    params = urlencode({
        "q": search_terms,
        "hl": "en-US",
        "gl": "US",
        "ceid": "US:en"
    })

    url = (
        "https://news.google.com/rss/search?"
        + params
    )

    request = Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    try:
        with urlopen(request, timeout=12) as response:
            content = response.read()

        root = ET.fromstring(content)
        articles = []

        for item in root.findall(".//item")[:limit]:
            title = item.findtext("title", "")
            link = item.findtext("link", "")
            date = item.findtext("pubDate", "")
            source = item.findtext("source", "")

            articles.append(
                f"Title: {title}\n"
                f"Publisher: {source}\n"
                f"Date: {date}\n"
                f"Link: {link}"
            )

        if not articles:
            return (
                "No relevant news retrieved. "
                "Do not invent external research."
            )

        return "\n\n".join(articles)

    except Exception as exc:
        return (
            "News retrieval unavailable. "
            f"Error type: {type(exc).__name__}. "
            "Use only the user-provided information "
            "and disclose this limitation."
        )
