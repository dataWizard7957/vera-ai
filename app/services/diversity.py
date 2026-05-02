REPETITIVE_OPENINGS = [
    "hey there",
    "hi there",
    "we noticed",
    "just checking",
    "wanted to let you know"
]


EXAMPLE_PHRASES = [
    "repeat visits dropped",
    "preventive recall reminders",
    "medicine refill orders slowed"
]


def diversity_penalty(text: str):

    text = text.lower().strip()

    penalty = 0

    for opening in REPETITIVE_OPENINGS:

        if text.startswith(opening):
            penalty += 5

    return penalty


def example_similarity_penalty(
    text: str
):

    text = text.lower()

    penalty = 0

    for phrase in EXAMPLE_PHRASES:

        if phrase in text:
            penalty += 3

    return penalty
