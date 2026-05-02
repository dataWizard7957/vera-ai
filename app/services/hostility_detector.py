HOSTILE_PATTERNS = [
    "stop",
    "unsubscribe",
    "leave me alone",
    "don't message",
    "not interested",
    "spam"
]


def is_hostile(text: str):

    text = text.lower()

    return any(p in text for p in HOSTILE_PATTERNS)