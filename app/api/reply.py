from fastapi import APIRouter

from app.services.conversation import handle_reply
from app.utils.logger import logger

router = APIRouter()


@router.post("/reply")
async def reply(payload: dict):

    merchant_id = payload.get("merchant_id")

    logger.info(f"Reply received for merchant: {merchant_id}")

    return handle_reply(payload)