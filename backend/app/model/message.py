from pydantic import BaseModel
from datetime import datetime

class Message(BaseModel):
    timestamp: datetime = datetime.now()
    question: str
    answer: str
    chat_id: int