
import random

from app.services.cta import (
    CTA_OPTIONS
)


BANNED_CTAS = [
    "reply yes",
    "yes",
    "book now"
]


def enforce_cta_diversity(
    message: dict
):

    current_cta = (
        message.get("cta", "")
        .strip()
        .lower()
    )

    # Force replacement
    if current_cta in BANNED_CTAS:

        message["cta"] = random.choice(
            CTA_OPTIONS
        )

    return message

