from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.session import get_db

app = FastAPI(

    title=settings.APP_NAME,
    description="AI-powered whatsapp Customer Agent",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "WhatsApp AI Customer Support Agent API",
        "status": "running"
    }


@app.get("/health")
def health_check(db: Session = Depends(get_db)):

    try:
        db.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "Supabase PostgreSQL connected"
        }

    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail="Database connection failed"
        )
