AUTO_REPLY_PATTERNS = [
    "busy",
    "call you later",
    "in a meeting",
    "not available",
    "away",
    "right now"
]


def is_auto_reply(text: str):

    text = text.lower()

    return any(p in text for p in AUTO_REPLY_PATTERNS)