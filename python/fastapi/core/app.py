from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .routes import api_router
from .settings import settings


def get_application():
    _app = FastAPI(
        title=settings.PROJECT_NAME,
        debug=settings.DEBUG,
        redoc_url=None
    )
    _app.include_router(api_router)
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()
