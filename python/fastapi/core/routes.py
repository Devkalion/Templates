from fastapi import APIRouter

from note.views import router as note_router

api_router = APIRouter(prefix='/api')
api_router.include_router(note_router)
