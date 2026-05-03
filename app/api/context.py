from fastapi import APIRouter
from datetime import datetime, timezone

from app.store.memory_store import memory_store

router = APIRouter()


@router.post("/context")
async def load_context(payload: dict):

    scope = payload.get("scope")
    context_id = payload.get("context_id")
    version = payload.get("version", 1)

    existing = memory_store["contexts"].get(context_id)

    # Reject stale or duplicate versions
    if existing and existing["version"] >= version:

        return {
            "accepted": False,
            "reason": "stale_version",
            "current_version": existing["version"]
        }

    # Store latest version
    memory_store["contexts"][context_id] = {
        "scope": scope,
        "version": version,
        "payload": payload.get("payload")
    }

    return {
        "accepted": True,
        "ack_id": f"ack_{context_id}_v{version}",
        "stored_at": datetime.now(
            timezone.utc
        ).isoformat()
    }
