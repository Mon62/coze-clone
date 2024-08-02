from pydantic import BaseModel
from datetime import datetime

class Message(BaseModel):
    time: datetime = datetime.now()
    question: str
    answer: str
    chat_id: int