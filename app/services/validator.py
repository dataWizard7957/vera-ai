BANNED_PHRASES = [
    "book now",
    "limited time",
    "exclusive deal",
    "don't miss out",
    "special offer just for you"
]

BANNED_COMPETITOR_PATTERNS = [
    "another salon",
    "competitor is offering",
    "other pharmacy"
]


def validate_response(message: dict):

    body = message.get("body", "").lower()

    for phrase in BANNED_PHRASES:
        if phrase in body:
            body = body.replace(phrase, "")

    for pattern in BANNED_COMPETITOR_PATTERNS:
        if pattern in body:
            message["body"] = (
                "Competition appears to be increasing locally. "
                "A loyalty-focused customer recall campaign may help improve retention. "
                "Want me to draft it?"
            )

    message["body"] = body.strip()

    if len(message.get("cta", "").split()) > 4:
        message["cta"] = "Reply YES"

    if "book now" in message["cta"].lower():
        message["cta"] = "Reply YES"

    return message