from persistent.db.base import Base

import asyncpg
from sqlalchemy import create_engine 
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from config import config

def async_connection() -> async_sessionmaker[AsyncSession]:
    engine = create_async_engine(url=config.DATABASE_URL_ASYNC)
    return async_sessionmaker(autocommit=False, autoflush=False, bind=engine)