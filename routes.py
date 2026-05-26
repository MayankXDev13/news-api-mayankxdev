import os
import logging
import asyncio

from fastapi import APIRouter, HTTPException

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api")

class TopHeadlinesSources(BaseModel):
    category: str
    country: str
    page_size: int = 100


@router.get("/top-headlines")
def get_top_headlines_sources(
    category: str = "general",
    country: str = "in",
    page_size: int = 100,
):
    return news_service.get_top_headlines_sources(category, country, page_size)
