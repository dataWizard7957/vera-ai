
KEYWORDS = ["yes", "start", "do it", "proceed"]

def detect_intent(text: str):
    text = text.lower()
    return any(k in text for k in KEYWORDS)
