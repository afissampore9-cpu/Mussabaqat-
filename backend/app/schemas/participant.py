from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ParticipantBase(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    age: Optional[int] = None
    category: Optional[str] = None

class ParticipantCreate(ParticipantBase):
    user_id: int
    competition_id: int

class Participant(ParticipantBase):
    id: int
    competition_id: int
    user_id: int
    status: str
    total_score: int
    rank: Optional[int]
    registration_date: datetime
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
