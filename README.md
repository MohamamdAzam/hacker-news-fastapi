
# Hacker News API with FastAPI

Welcome to the Hacker News API project! This is a simple and efficient API built with FastAPI that lets you fetch the top news stories from Hacker News. The goal here is to give you a quick and easy way to stay updated on the latest tech news while minimizing the load on the Hacker News API through caching.

## What You'll Find Here

- **Top News Endpoint**: Easily retrieve the top news stories, with a customizable count.
- **Caching**: Keeps the results around for 10 minutes to save on API calls.
- **Error Handling**: Smooth handling of issues when the Hacker News API is down or returns errors.

## Prerequisites

Before you get started, you'll need to have the following installed on your machine:

- [Python 3.8+](https://www.python.org/downloads/) - The programming language we're using.
- [Docker](https://docs.docker.com/get-docker/) - To run the application in a containerized environment.

## Getting Started

### Step 1: Clone the Repo

First, grab a copy of this repository to your local machine:

```sh
git clone https://github.com/MohamamdAzam/hacker-news-fastapi.git
cd hacker_news_api
```

### Step 2: Set Up Your Environment

Create a virtual environment to keep your dependencies isolated:

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Now, install the necessary Python packages:

```sh
pip install -r requirements.txt
```

## Running the App

With everything set up, you can run the FastAPI application:

```sh
uvicorn main:app --reload
```

You should see the app running at `http://127.0.0.1:8000`.

### Access the Endpoints

- **Welcome Message**: Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to check if everything's working.
- **Top News**: Head to [http://127.0.0.1:8000/top-news?count=10](http://127.0.0.1:8000/top-news?count=10) to fetch the top 10 news items.

## Dockerizing the Application

Want to run this app anywhere? Docker's got your back.

### Step 1: Build the Docker Image

```sh
docker build -t hacker-news-api .
```

### Step 2: Run the Docker Container

```sh
docker run -d -p 8000:8000 hacker-news-api
```

Now, visit `http://localhost:8000` in your browser or API client.

## Testing the API

You can test the API using Postman or `curl`:

- **Using curl**:

  ```sh
  curl -X GET "http://127.0.0.1:8000/top-news?count=5"
  ```

- **Using Postman**:

  1. Open Postman.
  2. Create a new GET request to `http://127.0.0.1:8000/top-news?count=5`.
  3. Hit "Send" and check out the results.

## Assumptions Made

- The Hacker News API is assumed to be stable. If it goes down, our error handling should keep things smooth.
- The cache is set to store 100 items for 10 minutes—just enough to balance between performance and resource usage.

## Wrapping Up

This project is a simple demonstration of building a FastAPI app that interacts with an external API, implements caching, and runs smoothly in Docker. Feel free to tweak, improve, or expand upon this foundation.
