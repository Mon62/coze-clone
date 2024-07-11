from fastapi import APIRouter, Depends, HTTPException, Security, Request, Form, File, UploadFile
from fastapi.encoders import jsonable_encoder
from supabase import Client
from utils.exceptions import BAD_REQUEST, FORBIDDEN, NOT_FOUND
from typing import Annotated, List
from database.db_service import get_supabase
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from model.message import Message

router = APIRouter(tags=["Message"], prefix="/message")

@router.get("/get_messages")
async def get_messages(
    chatbot_id: int,
    supabase: Annotated[Client, Depends(get_supabase)]
):
    try:
        messages = supabase.table("message").select("*").eq("chatbot_id", chatbot_id).order("timestamp", desc=True).execute().data
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
        data = jsonable_encoder(message)
        obj = supabase.table("message").insert(data).execute()
        return {"detail": "suuccessfully created message"}
    except:
        return BAD_REQUEST

