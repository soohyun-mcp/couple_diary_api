from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI(title="커플 다이어리 API")

# 데이터 모델 예시
class DiaryEntry(BaseModel):
    id: int
    title: str
    content: str
    images: Optional[List[str]] = []
    date: str

class Event(BaseModel):
    id: int
    name: str
    date: str
    description: Optional[str] = None

class CalendarItem(BaseModel):
    id: int
    title: str
    date: str
    description: Optional[str] = None

class SecretNote(BaseModel):
    id: int
    content: str
    created_at: str

# 엔드포인트 예시
@app.get("/diary", response_model=List[DiaryEntry])
def get_diary_entries():
    return []

@app.post("/diary", response_model=DiaryEntry)
def create_diary_entry(entry: DiaryEntry):
    return entry

@app.get("/events", response_model=List[Event])
def get_events():
    return []

@app.post("/events", response_model=Event)
def create_event(event: Event):
    return event

@app.get("/calendar", response_model=List[CalendarItem])
def get_calendar():
    return []

@app.post("/calendar", response_model=CalendarItem)
def add_calendar_item(item: CalendarItem):
    return item

@app.get("/secret-notes", response_model=List[SecretNote])
def get_secret_notes():
    return []

@app.post("/secret-notes", response_model=SecretNote)
def create_secret_note(note: SecretNote):
    return note 