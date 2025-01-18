from persistent.db import base
from sqlalchemy import create_engine
from config import config

from persistent.db.base import Base

def create_db():
    engine = create_engine(url=config.DATABASE_URL_SYNC)
    Base.metadata.create_all(engine)