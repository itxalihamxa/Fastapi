from token import ASYNC

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://admin:admin@localhost:5432/db"
# ASYNC_SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://admin:admin@localhost:5432/db"


engine = create_engine(SQLALCHEMY_DATABASE_URL, future=True)
# async_engine = create_async_engine(ASYNC_SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, future=True)
# AsyncSessionLocal = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# async def async_get_db():
#     async with AsyncSessionLocal() as db:
#         yield db
#         await db.commit()
#         db.close()