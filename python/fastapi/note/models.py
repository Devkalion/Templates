import sqlalchemy

from core.database import BaseModel


class Note(BaseModel):
    __tablename__ = 'notes'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    text = sqlalchemy.Column("text", sqlalchemy.String)
    completed = sqlalchemy.Column("completed", sqlalchemy.Boolean)
