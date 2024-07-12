from fastapi import APIRouter, Depends, HTTPException, Security, Request, Form, File, UploadFile
from fastapi.encoders import jsonable_encoder
from supabase import Client
from utils.exceptions import BAD_REQUEST, FORBIDDEN, NOT_FOUND
from typing import Annotated, List
from database.db_service import get_supabase
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from model.chatbot import Chatbot, LLM
from utils.optimize_prompt import optimize_prompt

router = APIRouter(tags=["Chatbot"], prefix="/chatbot")

@router.post("/create_chatbot")
async def create_chatbot(
    chatbot: Chatbot, 
    supabase: Annotated[Client, Depends(get_supabase)]
):
    try:
        data = jsonable_encoder(chatbot)
        obj = supabase.table("chatbot").insert(data).execute()
        chatbot_id = obj["data"][0]["id"]
        llm = LLM(chatbot_id=chatbot_id)
        llm_data = jsonable_encoder(llm)
        obj = supabase.table("llm").insert(llm_data).execute()

        return {"detail": "suuccessfully created chatbot"}
    
    except:
        return BAD_REQUEST

@router.get("/get_all_chatbots")
async def get_all_chatbots(
    supabase: Annotated[Client, Depends(get_supabase)]
):
    try:
        chatbots = supabase.table("chatbot").select("*").execute().data
        return chatbots
    except:
        return NOT_FOUND
    
@router.get("/get_chatbot/{chatbot_id}")
async def get_chatbot(
    chatbot_id: int,
    supabase: Annotated[Client, Depends(get_supabase)]
):
    try:
        chatbot = supabase.table("chatbot").select("*").eq("id", chatbot_id).execute().data
        return chatbot
    except:
        return NOT_FOUND

@router.patch("/update_chatbot")
async def update_chatbot(
    chatbot: Chatbot,
    supabase: Annotated[Client, Depends(get_supabase)]
):
    try:
        data = jsonable_encoder(chatbot)
        obj = supabase.table("chatbot").update(data).eq("id", chatbot.id).execute()
        return {"detail": "suuccessfully updated chatbot"}
    except:
        return BAD_REQUEST

@router.patch("/update_llm")
async def update_llm(
    llm: LLM,
    supabase: Annotated[Client, Depends(get_supabase)]
):
    try:
        data = jsonable_encoder(llm)
        obj = supabase.table("llm").update(data).eq("chatbot_id", llm.chatbot_id).execute()
        return {"detail": "suuccessfully updated llm"}
    except:
        return BAD_REQUEST
    
@router.delete("/delete_chatbot/{chatbot_id}")
async def delete_chatbot(
    chatbot_id: int,
    supabase: Annotated[Client, Depends(get_supabase)]
):
    try:
        obj = supabase.table("chatbot").delete().eq("id", chatbot_id).execute()
        return {"detail": "suuccessfully deleted chatbot"}
    except:
        return NOT_FOUND

@router.get("/prompt")
async def get_prompt(
    prompt: str
):
    return optimize_prompt(prompt)