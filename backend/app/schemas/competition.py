from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class CompetitionBase(BaseModel):
    name: str
    description: Optional[str] = None
    status: str = "draft"
    max_participants: int = 50
    juz_range: Optional[str] = None
    surah: Optional[str] = None
    difficulty_level: str = "intermediate"

class CompetitionCreate(CompetitionBase):
    judge_id: int

class CompetitionUpdate(BaseModel):
    name: Optional[str] = None
    status: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

class Competition(CompetitionBase):
    id: int
    judge_id: int
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
