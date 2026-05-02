
from pydantic import BaseModel

class ReplyRequest(BaseModel):
    merchant_id: str
    message: str
