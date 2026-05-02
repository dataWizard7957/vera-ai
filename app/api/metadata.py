
from fastapi import APIRouter

router = APIRouter()

@router.get("/metadata")
async def metadata():
    return {
        "bot_name": "Vera AI Assistant",
        "version": "1.0.0"
    }
