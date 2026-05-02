
from fastapi import APIRouter
from app.store.memory_store import memory_store

router = APIRouter()

@router.post("/context")
async def load_context(payload: dict):
    memory_store["contexts"].append(payload)
    return {
        "status": "stored",
        "count": len(memory_store["contexts"])
    }
