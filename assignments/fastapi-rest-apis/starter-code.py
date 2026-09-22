from fastapi import FastAPI

app = FastAPI(title="Resource API")

# In-memory storage
items = [
    {"id": 1, "title": "Python Basics", "description": "Learn the fundamentals of Python."},
    {"id": 2, "title": "FastAPI Intro", "description": "Build APIs with FastAPI."},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Resource API"}


@app.get("/items")
def get_items():
    return items


@app.post("/items")
def create_item(item: dict):
    item["id"] = len(items) + 1
    items.append(item)
    return item
