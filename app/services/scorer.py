from app.services.diversity import (
    diversity_penalty,
    example_similarity_penalty
)


GENERIC_PHRASES = [
    "special offer",
    "limited time",
    "exclusive deal",
    "book now",
    "don't miss",
    "act fast",
    "hurry up"
]


def score_message(
    message: dict,
    context: dict
):

    score = 50

    original_body = message.get(
        "body",
        ""
    )

    body = original_body.lower()

    merchant_name = (
        context.get("merchant", {})
        .get("name", "")
        .lower()
    )

    trigger_type = (
        context.get("trigger", {})
        .get("type", "")
        .lower()
    )

    category = (
        context.get("category", "")
        .lower()
    )

    # Penalize generic marketing language
    for phrase in GENERIC_PHRASES:

        if phrase in body:
            score -= 6

    # Reward merchant specificity
    if merchant_name and merchant_name in body:
        score += 8

    # Reward pricing specificity
    if "₹" in body:
        score += 6

    # Reward percentage specificity
    if "%" in body:
        score += 5

    # Reward trigger relevance
    trigger_keywords = [
        word
        for word in trigger_type.split("_")
        if len(word) > 3
    ]

    for keyword in trigger_keywords:

        if keyword in body:
            score += 3

    # Reward category terminology
    category_terms = {
        "salon": [
            "hair",
            "spa",
            "facial",
            "styling"
        ],
        "dentist": [
            "cleaning",
            "checkup",
            "oral",
            "dental"
        ],
        "pharmacy": [
            "refill",
            "medicine",
            "prescription",
            "delivery"
        ]
    }

    for term in category_terms.get(
        category,
        []
    ):

        if term in body:
            score += 2

    # Penalize overly long messages
    if len(body) > 320:
        score -= 8

    # Penalize too-short messages
    if len(body) < 60:
        score -= 6

    # Penalize repetitive CTA usage
    cta = (
        message.get("cta", "")
        .strip()
        .lower()
    )

    if cta == "reply yes":
        score -= 8

    if cta == "book now":
        score -= 10

    # Diversity penalties
    score -= diversity_penalty(body)

    score -= example_similarity_penalty(
        body
    )

    # Penalize fully lowercase responses
    if original_body == original_body.lower():
        score -= 4

    return score
