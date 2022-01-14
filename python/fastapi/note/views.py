from typing import Optional, List

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import Select

from core.database import get_db
from .models import Note
from .schemas import NoteSchema

router = APIRouter()


@router.get("/notes", response_model=List[NoteSchema])
async def read_root(db: AsyncSession = Depends(get_db)):
    statement: Select = select(Note)
    rows = await db.execute(statement)
    notes: List[Note] = list(rows.scalars())
    return notes


@router.get("/note/{note_id}", response_model=NoteSchema)
async def read_item(note_id: int, db: AsyncSession = Depends(get_db), q: Optional[str] = None):
    note = await db.get(Note, note_id)
    return note
