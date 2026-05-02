from openai import OpenAI
from app.config import settings

client = OpenAI(
    api_key=settings.GROQ_API_KEY,
    base_url=settings.BASE_URL,
    max_retries=1,
    timeout=5
)

def generate(prompt: str) -> str:
    response = client.chat.completions.create(
        model=settings.MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are Vera, an AI merchant engagement assistant. "
                    "Return ONLY valid JSON."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=300
    )

    return response.choices[0].message.content