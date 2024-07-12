from fastapi import APIRouter, Depends, FastAPI
from fastapi.encoders import jsonable_encoder
from supabase import Client
from utils.exceptions import BAD_REQUEST, FORBIDDEN, NOT_FOUND
from typing import Annotated, List
from database.db_service import get_supabase
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from model.message import Message

router = APIRouter(tags=["Message"], prefix="/message")

# global variable to store message history
app = FastAPI()
app.message_history = []

@router.get("/get_messages")
async def get_messages(
    chat_id: int,
    k: int,
    supabase: Annotated[Client, Depends(get_supabase)]
):
    try:
        messages = supabase.table("message").select("*").eq("chat_id", chat_id).order("time", desc=False).execute().data
        app.message_history = messages[-k:]
        print(app.message_history)
        return messages
    except:
        return NOT_FOUND

@router.delete("/delete_message/{message_id}")
async def delete_message(
    message_id: int,
    supabase: Annotated[Client, Depends(get_supabase)]
):
    try:
        obj = supabase.table("message").delete().eq("id", message_id).execute()
        return {"detail": "suuccessfully deleted message"}
    except:
        return NOT_FOUND
    
@router.patch("/update_message")
async def update_message(
    message: Message,
    supabase: Annotated[Client, Depends(get_supabase)]
):
    try:
        data = jsonable_encoder(message)
        obj = supabase.table("message").update(data).eq("id", message.id).execute()
        return {"detail": "suuccessfully updated message"}
    except:
        return BAD_REQUEST
    
@router.post("/create_message")
async def create_message(
    message: Message, 
    supabase: Annotated[Client, Depends(get_supabase)]
):
    try:
        print(app.message_history)
        return {"detail": "suuccessfully created message"}
    except:
        return BAD_REQUEST
