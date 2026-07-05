from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

from app.core.config import settings
from app.core.database import engine, Base
from app.api.routes import competitions, participants, judges, admin

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    logger.info("Database initialized")
    yield
    logger.info("Shutting down...")

app = FastAPI(
    title="Musabaqat - AI Qur'an Recitation Judge",
    description="Intelligent judging system for Qur'an recitation competitions",
    version="0.1.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(competitions.router, prefix="/api/competitions", tags=["Competitions"])
app.include_router(participants.router, prefix="/api/participants", tags=["Participants"])
app.include_router(judges.router, prefix="/api/judges", tags=["Judges"])
app.include_router(admin.router, prefix="/api/admin", tags=["Admin"])

@app.get("/")
async def root():
    return {"message": "Welcome to Musabaqat", "version": "0.1.0", "docs": "/docs"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
