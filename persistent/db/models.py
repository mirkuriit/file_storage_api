from pygments.lexer import default
from sqlalchemy import Text, ForeignKey, DateTime, BigInteger, Column, TIMESTAMP, Integer, Boolean
from sqlalchemy.orm import relationship, mapped_column
from datetime import datetime
from sqlalchemy.sql import func

from persistent.db.base import Base

class User(Base):
    __tablename__ = "user"
    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    ip_address = Column(Text, nullable=False)
    user_agent = Column(Text, default=None)
    files_count = Column(Integer, default=0)
    total_fle_size = Column(BigInteger, default=0)
    created_at = Column(TIMESTAMP,
                        server_default=func.now(),
                        onupdate=func.current_timestamp(),
                        nullable=False)

class FileOperation(Base):
    __tablename__ = "file_opeartion"
    id = Column(BigInteger, nullable=False, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    file_name = Column(Text, nullable=True, default=None)
    file_size = Column(Text, nullable=False, default=0)
    is_correct = Column(Boolean, nullable=False, default=0)
    long_link = Column(Text, nullable=False)
    short_link = Column(Text, nullable=False)






