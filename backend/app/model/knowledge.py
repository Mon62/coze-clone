from pydantic import BaseModel

class Knowledge(BaseModel):
    description: str
    name: str
    embed_model: str

class Knowledge_res(Knowledge):
    id:int

class File(BaseModel):
    knowledge_id: int
    name_in_storage: str
    name: str

class Document(BaseModel):
    content: str
    vector: list[float]
    file_id: int
    knowledge_id: int
    metadata: dict