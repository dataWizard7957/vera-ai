from fastapi import APIRouter
from datetime import datetime, timezone

router = APIRouter()

@router.get("/metadata")
async def metadata():

    return {
        "team_name": "ConversaAI",
        "team_members": ["Sakeena"],
        "model": "llama-3.1-8b-instant",
        "approach": "FastAPI based autonomous merchant engagement bot with trigger-driven messaging and conversation handling",
        "contact_email": "patelsakeenaakbar@gmail.com",
        "version": "1.0.0",
        "submitted_at": datetime.now(timezone.utc).isoformat()
    }
