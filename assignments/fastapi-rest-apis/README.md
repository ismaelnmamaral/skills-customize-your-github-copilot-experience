# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using the FastAPI framework to manage a collection of resources, such as books, movies, or students. By the end of this assignment, you will be able to create endpoints, validate request data, and document your API with FastAPI's automatic Swagger UI.

## 📝 Tasks

### 🛠️ Set Up a FastAPI App

#### Description
Create a new FastAPI application and configure the basic app structure.

#### Requirements
The completed app must:

- Import `FastAPI` from the `fastapi` package.
- Create an app instance named `app`.
- Add a root endpoint with `GET /` that returns a welcome message.
- Run the app locally with a development server.

Example:

```python
from fastapi import FastAPI

app = FastAPI(title="Resource API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Resource API"}
```

### 🛠️ Create a Resource Model

#### Description
Define a data model for the items your API will manage, and use it to validate incoming data.

#### Requirements
The completed app must:

- Define a Pydantic model with at least 3 fields.
- Use the model for request validation.
- Include fields such as `id`, `title`, and `description`, or similar values.
- Return the created resource as JSON.

### 🛠️ Implement CRUD Endpoints

#### Description
Add the main HTTP endpoints for creating, reading, updating, and deleting resources.

#### Requirements
The completed app must:

- Implement `GET /items` to list all resources.
- Implement `GET /items/{item_id}` to fetch a single item.
- Implement `POST /items` to create a new item.
- Implement `PUT /items/{item_id}` to update an item.
- Implement `DELETE /items/{item_id}` to remove an item.
- Use an in-memory list or dictionary to store data during the exercise.

### 🛠️ Add Validation and Error Handling

#### Description
Ensure the API behaves predictably when invalid data or missing resources are requested.

#### Requirements
The completed app must:

- Return a helpful error response for a missing item.
- Reject invalid input before creating or updating data.
- Use status codes like `200`, `201`, and `404` appropriately.

### 🛠️ Explore the Docs

#### Description
Use FastAPI’s built-in interactive documentation to test the API.

#### Requirements
The completed app must:

- Be accessible in the browser through the Swagger UI.
- Show the endpoints under the `/docs` route.
- Demonstrate the request and response examples for at least one endpoint.

## ✅ Challenge Extension

If you finish early, try one of these enhancements:

- Add filtering by query parameters, such as `?category=fiction`.
- Add a basic search endpoint.
- Use `response_model` to define the output schema.
- Add a small test file using `pytest` and `fastapi.testclient`.

## 💡 Tips

- Start with a simple in-memory model so you can focus on the API flow.
- Validate your code often by running the app and testing endpoints in the browser.
- Use the Swagger UI at `/docs` to explore the API without extra tooling.
