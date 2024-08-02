from fastapi import APIRouter, Depends, FastAPI
from fastapi.encoders import jsonable_encoder
from supabase import Client
from utils.exceptions import BAD_REQUEST, FORBIDDEN, NOT_FOUND
from typing import Annotated, List
from database.db_service import get_supabase
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from model.message import Message
from helper.generate import Gemini, GPT

router = APIRouter(tags=["Message"], prefix="/message")

# global variable to store message history
app = FastAPI()
app.message_history = []
app.instruction = ''

@router.get("/get_messages")
async def get_messages(
    chat_id: int,
    supabase: Annotated[Client, Depends(get_supabase)]
):
    try:
        messages = supabase.table("message").select("*").eq("chat_id", chat_id).order("time", desc=False).execute().data
        ins = supabase.table("chatbot").select('prompt').eq('id', chat_id).execute().data[0]
        app.instruction = ins['prompt']
        app.message_history = messages
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
    
@router.post("/send_message") 
async def send_message(
    chat_id: int,
    question: str,
    config_llm_id: int,
    supabase: Annotated[Client, Depends(get_supabase)]
):
    try:
        instruction = app.instruction
        config_llm = supabase.table("config_llm").select("*").eq("id", config_llm_id).execute().data[0]
        chats = app.message_history[-config_llm['dialog_round']:]
        answer = ""

        if config_llm['model_name'][:3] != 'GPT':
            model = Gemini(model_name=config_llm['model_name'], 
                           temperature=config_llm['temperature'], 
                           top_p=config_llm['top_p'], 
                           max_output_tokens=config_llm['max_length'])
            
            response = model.invoke(instruction=instruction,
                                    question=question,
                                    chats=chats,
                                    context='')
            answer = response.text

        else:
            model = GPT(model_name=config_llm['model_name'], 
                        temperature=config_llm['temperature'], 
                        top_p=config_llm['top_p'], 
                        frequency_penalty=config_llm['frequency_penalty'], 
                        presence_penalty=config_llm['presence_penalty'], 
                        max_length=config_llm['max_length'], 
                        output_format=config_llm['output_format'])
            
            response = model.invoke(instruction=instruction,
                                    question=question,
                                    chats=chats,
                                    context='')
            answer = response.choices[0].message.content
    
        message = Message(chat_id=chat_id,
                          question=question,
                          answer=answer)
        
        supabase.table("message").insert(jsonable_encoder(message)).execute()

        return answer
    except:
        return BAD_REQUEST
    
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