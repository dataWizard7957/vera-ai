from app.store.memory_store import memory_store


def get_conversation_state(merchant_id: str):

    if merchant_id not in memory_store["conversations"]:

        memory_store["conversations"][merchant_id] = {
            "messages_sent": 0,
            "last_trigger": "",
            "last_message": "",
            "last_action": "",
            "auto_reply_count": 0,
            "hostile_count": 0,
            "intent_detected": False,
            "conversation_ended": False,

            # NEW
            "sent_messages": [],
            "used_suppression_keys": []
        }

    return memory_store["conversations"][merchant_id]


def update_conversation_state(
    merchant_id: str,
    updates: dict
):

    state = get_conversation_state(merchant_id)

    state.update(updates)

    memory_store["conversations"][merchant_id] = state