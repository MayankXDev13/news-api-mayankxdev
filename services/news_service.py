from datetime import datetime, timedelta

from newsapi import NewsApiClient
from config import NEWS_API_KEY

newsapi = NewsApiClient(api_key=NEWS_API_KEY)

COUNTRIES_LANGUAGES = {
    "in": "en",
    "us": "en",
    "au": "en",
    "ru": "ru",
    "fr": "fr",
    "gb": "en",
}

CATEGORIES = [
    "business",
    "entertainment",
    "general",
    "health",
    "science",
    "sports",
    "technology",
]

SOURCES = ["bbc-news", "cnn", "fox-news", "google-news"]


def get_top_headlines(
    category: str = "general",
    country: str = "in",
    page_size: int = 100,
):
    try:
        return newsapi.get_top_headlines(
            category=category,
            language=COUNTRIES_LANGUAGES[country],
            country=country,
            page_size=page_size,
        )
    except Exception as e:
        return {"error": str(e)}


def get_everything(
    q=None,
    sources=None,
    domains=None,
    from_param=None,
    language=None,
    sort_by="publishedAt",
    page_size=100,
):
    if from_param is None:
        from_param = (
            datetime.now() - timedelta(days=1)
        ).date().isoformat()

    return newsapi.get_everything(
        q=q,
        sources=sources,
        domains=domains,
        from_param=from_param,
        language=language,
        sort_by=sort_by,
        page_size=page_size,
    )


def get_sources(category=None, country=None, language=None):
    return newsapi.get_sources(
        category=category,
        country=country,
        language=COUNTRIES_LANGUAGES[country],
    )