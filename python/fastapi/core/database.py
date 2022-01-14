import sqlalchemy
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, as_declarative, declared_attr

from .settings import settings

engine = create_async_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
)

metadata = sqlalchemy.MetaData(bind=engine)


@as_declarative(metadata=metadata)
class BaseModel:

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


async def get_db():
    async with SessionLocal() as session:
        async with session.begin():
            yield session
