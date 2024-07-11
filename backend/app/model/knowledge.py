from pydantic import BaseModel

class Knowledge(BaseModel):
    description: str
    user_id: int
    name: str
    embed_model: str

class File(BaseModel):
    knowledge_id: int
    url: str
    name: str

class Document(BaseModel):
    content: str
    vector: list[float]
    file_id: int
    knowledge_id: int
    metadata: dict