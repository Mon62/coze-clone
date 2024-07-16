from fastapi import APIRouter, Depends, Security
from supabase import Client
from utils.exceptions import BAD_REQUEST, FORBIDDEN, NOT_FOUND
from typing import Annotated, List
from database.db_service import get_supabase
from utils.auth import get_id
from model.knowledge import Knowledge, Knowledge_res
from utils.embedding import get_document

router = APIRouter(tags=["Knowledge"], prefix='/knowledge')

@router.post("/create")
async def create_knowledge(
    knowledge: Knowledge, 
    user_id: Annotated[str, Security(get_id)],
    supabase: Annotated[Client, Depends(get_supabase)]
):
    try:
        if "gpt" in knowledge.embed_model:
            pass
        elif "gemini" in knowledge.embed_model:
            pass
        else:
            raise BAD_REQUEST
        supabase.table("knowledge").insert(
            {"description": knowledge.description,"name": knowledge.name,"embed_model":knowledge.embed_model, "user_id": user_id}
        ).execute()
        return {"detail": "Knowledge created"}
    except:
        raise BAD_REQUEST

@router.get("/get_all")
async def get_all(
    user_id: Annotated[str, Security(get_id)],
    supabase: Annotated[Client, Depends(get_supabase)]
)-> List[Knowledge_res]:
    try:
        res = supabase.table("knowledge").select("*").match({"user_id" : user_id}).execute().dict()["data"]
        return res
    except:
        raise BAD_REQUEST

@router.get("/get_detail")
async def get_detail(
    user_id: Annotated[str, Security(get_id)],
    supabase: Annotated[Client, Depends(get_supabase)],
    knowledge_id:int
):
    res = supabase.table("knowledge").select("*").match({"user_id" : user_id,"id":knowledge_id}).execute().dict()["data"]
    if res == []:
        raise NOT_FOUND
    
    res = (
            supabase.table("knowledge")
            .select("*, file(*)")
            .eq("id", knowledge_id)
            .execute()
            .dict()["data"][0]
        )
    return res

@router.patch("/modify")
async def modify_knowledge(
    knowledge: Knowledge, 
    knowledge_id:int,
    user_id: Annotated[str, Security(get_id)],
    supabase: Annotated[Client, Depends(get_supabase)]
):
    res = supabase.table("knowledge").select("*").match({"user_id" : user_id,"id":knowledge_id}).execute().dict()["data"]
    if res == []:
        raise NOT_FOUND
    
    try:
        supabase.table("knowledge").update(
            {"description": knowledge.description,"name": knowledge.name,"embed_model":knowledge.embed_model}
        ).eq("id", knowledge_id).execute()
        return {"detail": "Knowledge modify"}
    except:
        raise BAD_REQUEST
    

@router.get("/document", )
async def document(
    supabase: Annotated[Client, Depends(get_supabase)],
    id: Annotated[str, Security(get_id)],
    knowledge_id:int,
    input:str
):  

    res = await get_document(supabase,knowledge_id,input)
    return res


# # delete knowledge
# @router.delete("/delete", description="Delete knowledge")
# async def delete_knowledge(
#     supabase: Annotated[Client, Depends(get_supabase)],
#     user_id: Annotated[str, Security(get_id)],
#     knowledge_id: int,
# ):
#     res = supabase.table("knowledge").select("*").match({"user_id" : user_id,"id":knowledge_id}).execute().dict()["data"]
#     if res ==[]:
#         raise NOT_FOUND
    
#     try:
#         supabase.table("documents").delete().eq("knowledge_id", knowledge_id).execute()
#         l
#         delete_file(supabase,user_id,)
#         supabase.table("knowledge").delete().eq("id", knowledge_id).execute()
#         return {"detail": "Knowledge deleted"}
#     except:
#         raise BAD_REQUEST