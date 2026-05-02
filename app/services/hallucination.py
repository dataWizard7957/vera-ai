BANNED_PATTERNS = [
    "guaranteed",
    "best in india",
    "no.1"
]


def has_hallucination(text: str):

    text = text.lower()

    return any(
        pattern in text
        for pattern in BANNED_PATTERNS
    )