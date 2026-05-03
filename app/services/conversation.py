from app.services.auto_reply import is_auto_reply
from app.services.intent_detector import detect_intent
from app.services.hostility_detector import is_hostile

from app.services.state_manager import (
    get_conversation_state,
    update_conversation_state
)

from app.utils.logger import logger


def handle_reply(payload: dict):

    merchant_id = payload.get("merchant_id")
    logger.info(f"Processing reply for merchant: {merchant_id}")

    text = payload.get("message", "")

    state = get_conversation_state(merchant_id)

    # Already ended
    if state["conversation_ended"]:

        return {
            "action": "end",
            "rationale": "Conversation already closed."
        }

    # Hostile user
    if is_hostile(text):

        update_conversation_state(
            merchant_id,
            {
                "hostile_count": state["hostile_count"] + 1,
                "conversation_ended": True
            }
        )

        return {
            "action": "end",
            "rationale": "Merchant requested to stop messaging."
        }

    # Auto reply handling
    if is_auto_reply(text):

        auto_reply_count = state["auto_reply_count"] + 1

        update_conversation_state(
            merchant_id,
            {
                "auto_reply_count": auto_reply_count
            }
        )

        # Too many auto replies
        if auto_reply_count >= 2:

            update_conversation_state(
                merchant_id,
                {
                    "conversation_ended": True
                }
            )

            return {
                "action": "end",
                "rationale": "Repeated auto replies detected."
            }

        return {
            "action": "wait",
            "wait_seconds": 14400,
            "rationale": "Detected business auto reply."
        }

    # Merchant interested
    if detect_intent(text):

        update_conversation_state(
            merchant_id,
            {
                "intent_detected": True
            }
        )

        return {
            "action": "send",
            "body": (
                "Great — I can prepare that campaign draft for you today."
            ),
            "cta": "binary_confirm_cancel",
            "rationale": (
                "Merchant showed clear execution intent."
            )
        }

    # Neutral response
    return {
        "action": "wait",
        "wait_seconds": 3600,
        "rationale": "Waiting for clearer merchant intent."
    }
