from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, Enum
from datetime import datetime
from app.core.database import Base
import enum

class CompetitionStatus(str, enum.Enum):
    DRAFT = "draft"
    ACTIVE = "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class Competition(Base):
    __tablename__ = "competitions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String, default=CompetitionStatus.DRAFT.value)
    start_date = Column(DateTime, nullable=True)
    end_date = Column(DateTime, nullable=True)
    max_participants = Column(Integer, default=50)
    judge_id = Column(Integer, nullable=False)
    juz_range = Column(String, nullable=True)
    surah = Column(String, nullable=True)
    difficulty_level = Column(String, default="intermediate")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
