from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services import news_service

router = APIRouter(prefix="/api/news", tags=["News"])


class TopHeadlinesRequest(BaseModel):
    category: str = "general"
    country: str = "in"
    page_size: int = 100


class EverythingRequest(BaseModel):
    q: str | None = None
    sources: str | None = None
    domains: str | None = None
    language: str | None = None
    sort_by: str = "publishedAt"
    page_size: int = 100


@router.get("/top-headlines")
def top_headlines(
    category: str = "general",
    country: str = "in",
    page_size: int = 100,
):
    return news_service.get_top_headlines(
        category=category,
        country=country,
        page_size=page_size,
    )


@router.get("/everything")
def everything(
    q: str | None = None,
    sources: str | None = None,
    domains: str | None = None,
    language: str | None = None,
    sort_by: str = "publishedAt",
    page_size: int = 100,
):
    return news_service.get_everything(
        q=q,
        sources=sources,
        domains=domains,
        language=language,
        sort_by=sort_by,
        page_size=page_size,
    )


@router.get("/sources")
def sources(
    category: str | None = None,
    country: str | None = None,
    language: str | None = None,
):
    return news_service.get_sources(
        category=category,
        country=country,
        language=language,
    )