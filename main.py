from fastapi import FastAPI
from routes import router as news_router

app = FastAPI(title="News API - mayankxdev")

app.include_router(news_router)