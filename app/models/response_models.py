
from pydantic import BaseModel

class ComposeResponse(BaseModel):
    body: str
    cta: str
    send_as: str
    suppression_key: str
    rationale: str
