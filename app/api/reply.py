from fastapi import APIRouter

from app.services.conversation import handle_reply
from app.utils.logger import logger

router = APIRouter()


@router.post("/reply")
async def reply(payload: dict):

    merchant_id = payload.get("merchant_id")
    conversation_id = payload.get("conversation_id")

    logger.info(
        f"Reply received | merchant={merchant_id} | conversation={conversation_id}"
    )

    response = handle_reply(payload)

    return response
