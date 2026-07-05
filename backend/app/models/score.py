from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Float
from datetime import datetime
from app.core.database import Base

class Score(Base):
    __tablename__ = "scores"
    id = Column(Integer, primary_key=True, index=True)
    recitation_id = Column(Integer, ForeignKey("recitations.id"), nullable=False)
    participant_id = Column(Integer, ForeignKey("participants.id"), nullable=False)
    competition_id = Column(Integer, ForeignKey("competitions.id"), nullable=False)
    round_id = Column(Integer, ForeignKey("rounds.id"), nullable=False)
    hifz_score = Column(Integer, default=0)
    tajweed_score = Column(Integer, default=0)
    makharij_score = Column(Integer, default=0)
    fluency_score = Column(Integer, default=0)
    total_score = Column(Integer, default=0)
    hifz_feedback = Column(Text, nullable=True)
    tajweed_feedback = Column(Text, nullable=True)
    makharij_feedback = Column(Text, nullable=True)
    fluency_feedback = Column(Text, nullable=True)
    summary_feedback = Column(Text, nullable=True)
    mistakes_log = Column(Text, nullable=True)
    judge_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    evaluated_at = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
