from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class RecitationBase(BaseModel):
    verse_assigned: str
    audio_file_path: str
    audio_duration: Optional[float] = None

class RecitationCreate(RecitationBase):
    participant_id: int
    round_id: int
    competition_id: int

class Recitation(RecitationBase):
    id: int
    participant_id: int
    round_id: int
    competition_id: int
    transcription: Optional[str]
    status: str
    mistakes_detected: Optional[str]
    submitted_at: datetime
    evaluated_at: Optional[datetime]
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
