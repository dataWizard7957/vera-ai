from fastapi import APIRouter
import time

router = APIRouter()

START_TIME = time.time()

@router.get("/healthz")
async def healthz():

    uptime = int(time.time() - START_TIME)

    return {
        "status": "ok",
        "uptime_seconds": uptime,
        "contexts_loaded": {
            "category": 0,
            "merchant": 0,
            "customer": 0,
            "trigger": 0
        }
    }
