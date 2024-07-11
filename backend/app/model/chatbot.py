from pydantic import BaseModel

class Chatbot(BaseModel):
    prompt: str
    user_id: int
    knowledges: list[int]
    name: str

class LLM(BaseModel):
    temperature: float = 0.5
    top_p: float = 1
    frequency_penalty: float = 0
    presence_penalty: float = 0
    dialog_round: int = 3
    max_length: int = 1024
    output_format: str = 'text'
    config_type: int = 1
    llm_type: str = 'gemini-1.5'
    chatbot_id: int