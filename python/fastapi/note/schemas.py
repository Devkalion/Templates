from pydantic import BaseModel


class NoteIn(BaseModel):
    text: str
    completed: bool


class NoteSchema(BaseModel):
    id: int
    text: str
    completed: bool

    class Config:
        orm_mode = True
