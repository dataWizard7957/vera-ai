
from pydantic import BaseModel

class TriggerContext(BaseModel):
    trigger_type: str
