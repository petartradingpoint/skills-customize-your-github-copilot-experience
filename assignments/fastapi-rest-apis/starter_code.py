from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List
from uuid import uuid4


class NoteCreate(BaseModel):
    title: str = Field(..., min_length=1)
    content: Optional[str] = ""


class Note(NoteCreate):
    id: str


app = FastAPI()

_db = {}


@app.post("/notes", response_model=Note, status_code=201)
def create_note(note: NoteCreate):
    nid = str(uuid4())
    record = Note(id=nid, **note.dict())
    _db[nid] = record
    return record


@app.get("/notes", response_model=List[Note])
def list_notes(skip: int = 0, limit: int = 10, q: Optional[str] = None):
    items = list(_db.values())
    if q:
        ql = q.lower()
        items = [n for n in items if ql in n.title.lower() or ql in (n.content or "").lower()]
    return items[skip : skip + limit]


@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: str):
    note = _db.get(note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@app.put("/notes/{note_id}", response_model=Note)
def update_note(note_id: str, update: NoteCreate):
    if note_id not in _db:
        raise HTTPException(status_code=404, detail="Note not found")
    updated = Note(id=note_id, **update.dict())
    _db[note_id] = updated
    return updated


@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: str):
    if note_id not in _db:
        raise HTTPException(status_code=404, detail="Note not found")
    del _db[note_id]
    return None
