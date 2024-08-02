from fastapi import APIRouter, Depends, HTTPException, Security, Request, Form, File, UploadFile
from fastapi.encoders import jsonable_encoder
from supabase import Client
from utils.exceptions import BAD_REQUEST, FORBIDDEN, NOT_FOUND
from typing import Annotated, List
from database.db_service import get_supabase
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from model.chatbot import Chatbot, LLM, ChatbotBase
from helper.optimize_prompt import optimize_prompt
from utils.auth import get_id

router = APIRouter(tags=["Chatbot"], prefix="/chatbot")

models = ['gemini-1.5-pro', 'gemini-1.5-flash', 'gpt-3.5-turbo-0125']

@router.post("/create_chatbot")
async def create_chatbot(
    chatbot: ChatbotBase,
    user_id: Annotated[str, Security(get_id)], 
    supabase: Annotated[Client, Depends(get_supabase)]
):
    try:
        data = jsonable_encoder(chatbot)
        data["user_id"] = user_id
        obj = supabase.table("chatbot").insert(data).execute().data
        chatbot_id = obj[0]["id"]
        for model in models:
            llm = LLM(chatbot_id=chatbot_id, model_name=model)
            llm_data = jsonable_encoder(llm)
            print (llm_data)
            supabase.table("config_llm").insert(llm_data).execute()

        return {"detail": "suuccessfully created chatbot"}
    
    except:
        return BAD_REQUEST

@router.get("/get_all_chatbots")
async def get_all_chatbots(
    user_id: Annotated[str, Security(get_id)],
    supabase: Annotated[Client, Depends(get_supabase)]
):
    try:
        chatbots = supabase.table("chatbot").select("*").eq("user_id", user_id).execute().data
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
        obj = supabase.table("llm").update(data).eq("id", llm.id).execute()
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

@router.post("/optimize_prompt")
async def optimize(
    prompt: str
):
    try:
        res = optimize_prompt(prompt)
        return optimize_prompt(res)
    except:
        return BAD_REQUEST