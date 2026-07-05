from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ScoreBase(BaseModel):
    hifz_score: int = 0
    tajweed_score: int = 0
    makharij_score: int = 0
    fluency_score: int = 0

class ScoreCreate(ScoreBase):
    recitation_id: int
    participant_id: int
    competition_id: int
    round_id: int
    judge_id: Optional[int] = None

class Score(ScoreBase):
    id: int
    recitation_id: int
    participant_id: int
    competition_id: int
    round_id: int
    total_score: int
    hifz_feedback: Optional[str]
    tajweed_feedback: Optional[str]
    makharij_feedback: Optional[str]
    fluency_feedback: Optional[str]
    summary_feedback: Optional[str]
    mistakes_log: Optional[str]
    judge_id: Optional[int]
    evaluated_at: datetime
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
