# News API

A FastAPI proxy for [NewsAPI.org](https://newsapi.org/).

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file:

```
NEWS_API_KEY=your_api_key_here
```

## Run

```bash
uvicorn main:app --reload
```

Server starts at `http://127.0.0.1:8000`.

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/news/top-headlines` | Top headlines by category/country |
| GET | `/api/news/everything` | Search all articles |
| GET | `/api/news/sources` | Available news sources |

### Query Parameters

**`/top-headlines`**
- `category` — `business`, `entertainment`, `general`, `health`, `science`, `sports`, `technology` (default: `general`)
- `country` — `in`, `us`, `au`, `ru`, `fr`, `gb` (default: `in`)
- `page_size` — max articles (default: `100`)

**`/everything`**
- `q` — keyword search
- `sources` — comma-separated source IDs
- `domains` — comma-separated domains
- `language` — `en`, `fr`, `ru`, etc.
- `sort_by` — `relevancy`, `popularity`, `publishedAt` (default)
- `page_size` — max articles (default: `100`)

**`/sources`**
- `category` — filter by category
- `country` — filter by country

## Docs

OpenAPI docs at `/docs` or `/redoc`.