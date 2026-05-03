from fastapi import APIRouter

from app.services.composer import compose_message

from app.services.state_manager import (
    get_conversation_state,
    update_conversation_state
)

from app.services.suppression import (
    is_duplicate_message,
    is_duplicate_suppression_key
)

router = APIRouter()


@router.post("/tick")
async def tick(payload: dict):

    merchant_id = payload.get("merchant_id")

    state = get_conversation_state(merchant_id)

    # Conversation already ended
    if state["conversation_ended"]:

        return {
            "actions": []
        }

    # Prevent excessive messaging
    if state["messages_sent"] >= 3:

        return {
            "actions": []
        }

    # Generate message
    message = compose_message(payload)

    # Prevent duplicate message body
    if is_duplicate_message(
        merchant_id,
        message["body"]
    ):

        return {
            "actions": []
        }

    # Prevent duplicate suppression campaigns
    if is_duplicate_suppression_key(
        merchant_id,
        message["suppression_key"]
    ):

        return {
            "actions": []
        }

    # Save sent message history
    state["sent_messages"].append(
        message["body"]
    )

    state["used_suppression_keys"].append(
        message["suppression_key"]
    )

    # Update conversation state
    update_conversation_state(
        merchant_id,
        {
            "messages_sent": state["messages_sent"] + 1,
            "last_message": message["body"],
            "last_action": "send",
            "sent_messages": state["sent_messages"],
            "used_suppression_keys": state[
                "used_suppression_keys"
            ]
        }
    )

    return {
        "actions": [
            message
        ]
    }
