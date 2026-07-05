from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Float
from datetime import datetime
from app.core.database import Base

class Recitation(Base):
    __tablename__ = "recitations"
    id = Column(Integer, primary_key=True, index=True)
    participant_id = Column(Integer, ForeignKey("participants.id"), nullable=False)
    round_id = Column(Integer, ForeignKey("rounds.id"), nullable=False)
    competition_id = Column(Integer, ForeignKey("competitions.id"), nullable=False)
    verse_assigned = Column(Text, nullable=False)
    audio_file_path = Column(String, nullable=False)
    audio_duration = Column(Float, nullable=True)
    transcription = Column(Text, nullable=True)
    status = Column(String, default="submitted")
    mistakes_detected = Column(Text, nullable=True)
    submitted_at = Column(DateTime, default=datetime.utcnow)
    evaluated_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
