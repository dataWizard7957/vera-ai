from app.services.state_manager import (
    get_conversation_state
)


def is_duplicate_message(
    merchant_id: str,
    message_body: str
):

    state = get_conversation_state(merchant_id)

    previous_messages = state.get(
        "sent_messages",
        []
    )

    normalized_message = (
        message_body.strip().lower()
    )

    normalized_previous = [
        msg.strip().lower()
        for msg in previous_messages
    ]

    return normalized_message in normalized_previous


def is_duplicate_suppression_key(
    merchant_id: str,
    suppression_key: str
):

    state = get_conversation_state(merchant_id)

    used_keys = state.get(
        "used_suppression_keys",
        []
    )

    return suppression_key in used_keys