from fastapi import FastAPI, HTTPException, Query
import requests
from cachetools import TTLCache
from cachetools import cached

app = FastAPI()

# Cache to store top news for 10 minutes (600 seconds)
cache = TTLCache(maxsize=100, ttl=600)

@cached(cache)
def get_top_news(count: int):
    response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
    if response.status_code != 200:
        raise HTTPException(status_code=503, detail="Hacker News API is unavailable")
    
    story_ids = response.json()[:count]
    stories = []

    for story_id in story_ids:
        story_response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json')
        if story_response.status_code == 200:
            stories.append(story_response.json())
        else:
            raise HTTPException(status_code=503, detail="Failed to fetch story details")
    
    return stories

@app.get("/top-news/")
def top_news(count: int = Query(10, gt=0)):
    try:
        return get_top_news(count)  
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    return {"message": "Welcome to the Hacker News API."}
