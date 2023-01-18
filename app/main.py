from fastapi import FastAPI, Depends, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pathlib import Path
from app.database import get_db
from app.models import Note

BASE_PATH = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_PATH / "templates"))

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/home", response_class=HTMLResponse)
async def home_page(req: Request, db: Session = Depends(get_db)):
    notes = db.query(Note).all()
    return templates.TemplateResponse("home.html", {'request': req, 'notes': notes})

@app.post("/notes")
async def new_note(req: Request, db: Session = Depends(get_db)):
    form_data = await req.form()
    title = form_data['title']
    content = form_data['content']
    note = {'content': content, "owner_id": 1, "title": title}
    new_note = Note(**note)
    db.add(new_note)
    db.commit()
    return templates.TemplateResponse("note.html", {"request": req})

@app.post("/notes/{id}", response_class=RedirectResponse)
async def save_note(id: int, req: Request, db: Session = Depends(get_db)):
    form_data = await req.form()
    content = form_data["noteContent"]
    note_query = db.query(Note).filter(Note.id == id)
    note_query.update({"content": content}, synchronize_session=False)
    db.commit()
    return templates.TemplateResponse("note.html", {"request": req})

@app.get("/notes/{id}", response_class=HTMLResponse)
async def delete_note(id: int, req: Request, db: Session = Depends(get_db)):
    note_query = db.query(Note).filter(Note.id == id).first()
    db.delete(note_query)
    db.commit()
    return templates.TemplateResponse("note.html", {"request": req})
