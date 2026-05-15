# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Students will build a small RESTful API using the FastAPI framework. They will design Pydantic models, implement CRUD endpoints, add basic filtering and pagination, and write simple tests.

## 📝 Tasks

### 🛠️ Implement a Notes CRUD API

#### Description
Create a REST API to manage simple `Note` resources. Implement endpoints to create, read, update, list, and delete notes.

#### Requirements
Completed program should:

- Expose endpoints: `POST /notes`, `GET /notes`, `GET /notes/{id}`, `PUT /notes/{id}`, `DELETE /notes/{id}`
- Use Pydantic models for request/response validation
- Return appropriate HTTP status codes (201 for creation, 204 for delete, 404 when missing)
- Store data in-memory for this exercise (a dictionary is sufficient)
- Validate inputs (e.g., non-empty `title`)

Example request (create):

```bash
curl -X POST "http://localhost:8000/notes" \
  -H "Content-Type: application/json" \
  -d '{"title": "Shopping", "content": "Buy milk"}'
```

Example response (201):

```json
{
  "id": "e7a1f2d2-...",
  "title": "Shopping",
  "content": "Buy milk"
}
```

### 🛠️ Add filtering and pagination

#### Description
Add optional query parameters to `GET /notes` to allow searching by text and basic pagination via `skip` and `limit`.

#### Requirements

- Support `q` (search string) to filter notes by title or content
- Support `skip` and `limit` query params for pagination

### 🛠️ Write tests using TestClient

#### Description
Write a small test suite that verifies the core endpoints (create, get, list, update, delete).

#### Requirements

- Include at least one test that creates a note and verifies it can be retrieved
- Test error responses for missing notes

---

## Setup & Run

1. Create a Python 3.9+ virtual environment.
2. Install dependencies:

```bash
pip install -r assignments/fastapi-rest-apis/requirements.txt
```

3. Run the app (from the project root):

```bash
cd assignments/fastapi-rest-apis
uvicorn starter_code:app --reload --port 8000
```

4. Open the interactive docs at `http://localhost:8000/docs` to explore the API.

## Starter Code

See the starter FastAPI app in `assignments/fastapi-rest-apis/starter-code.py`.
