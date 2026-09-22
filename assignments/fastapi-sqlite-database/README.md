# 📘 Assignment: FastAPI and SQLite

## 🎯 Objective

Create a small REST API that stores and retrieves information from a SQLite database using FastAPI. This assignment helps students connect API endpoints to persistent data and practice data validation, database queries, and CRUD operations.

## 📝 Tasks

### 🛠️ Set Up the Database

#### Description
Create a SQLite database and define a table for the records your API will manage.

#### Requirements
The completed program must:

- Import `sqlite3` and create a connection to a local database file.
- Create a table named `items` or `books` with at least 3 columns.
- Include a primary key field and at least two additional fields such as `title` and `description`.
- Initialize the database when the app starts.

Example:

```python
import sqlite3

conn = sqlite3.connect("items.db")
cursor = conn.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT
    )
    """
)
conn.commit()
```

### 🛠️ Build the API Endpoints

#### Description
Use FastAPI to expose endpoints for creating, reading, updating, and deleting database records.

#### Requirements
The completed app must:

- Implement `GET /items` to list all records.
- Implement `GET /items/{item_id}` to fetch a single record.
- Implement `POST /items` to insert a new record.
- Implement `PUT /items/{item_id}` to update an existing record.
- Implement `DELETE /items/{item_id}` to remove a record.
- Return JSON data with the correct HTTP status codes.

### 🛠️ Validate Input and Handle Errors

#### Description
Make sure invalid data is rejected and missing records return clear responses.

#### Requirements
The completed app must:

- Require meaningful fields such as `title` and `description` when creating or updating data.
- Return `404` for a missing item.
- Return `201` for successful creation.
- Return `200` for successful updates and reads.

### 🛠️ Connect the API to SQLite Queries

#### Description
Write the logic that reads and writes data between FastAPI endpoints and the database.

#### Requirements
The completed app must:

- Use `sqlite3` queries to insert, select, update, and delete data.
- Fetch results as Python dictionaries or JSON-compatible values.
- Close or reuse database connections safely.
- Avoid repeating the same database setup logic across endpoints.

### 🛠️ Test the API in Swagger UI

#### Description
Run the API locally and use the interactive documentation to validate each endpoint.

#### Requirements
The completed app must:

- Be available through a local development server.
- Show the API documentation in `/docs`.
- Test at least one create request and one read request using the Swagger interface.
- Confirm that data persists between requests.

## ✅ Challenge Extension

If you finish early, try one of these enhancements:

- Add a search endpoint to find items by title.
- Filter records by a query parameter such as `?category=books`.
- Add a `created_at` timestamp column.
- Create a `pytest` test file for the API endpoints.

## 💡 Tips

- Start with one simple table and a few endpoints before adding more features.
- Test your endpoints with Swagger UI so you can debug responses quickly.
- Keep the database logic organized so it is easy to reuse across requests.
