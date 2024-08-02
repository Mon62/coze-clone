from fastapi import APIRouter, Depends, Security, UploadFile, HTTPException, status
from supabase import Client
from utils.exceptions import BAD_REQUEST, FORBIDDEN, NOT_FOUND
from typing import Annotated, List
from database.db_service import get_supabase
from utils.auth import get_id
import uuid
from model.knowledge import File
from utils.embedding import embedding_file_gpt, get_document

router = APIRouter(tags=["File"], prefix='/file')


@router.post("", )
async def upload_file(
    supabase: Annotated[Client, Depends(get_supabase)],
    id: Annotated[str, Security(get_id)],
    knowledge_id:int,
    file: UploadFile,
):
    """
    Upload file
    - **name**: each file must have a name
    - **file**: a file pdf
    """ 
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only PDF file is accepted",
        )
    res = supabase.table("knowledge").select("*").match({"user_id" : id,"id":knowledge_id}).execute().dict()["data"]
    if res ==[]:
        raise NOT_FOUND
    try:
        f = await file.read()
        res = supabase.table("file").insert(
            {"name": file.filename,"knowledge_id":knowledge_id}
        ).execute()
        file_id = res.data[0]['id']

        supabase.storage.from_("file").upload(
            path= str(file_id), file=f, file_options={"content-type": "application/pdf"}
        )

        return res.data[0]
    except:
        raise BAD_REQUEST
    
@router.get("", )
async def embed_file(
    supabase: Annotated[Client, Depends(get_supabase)],
    id: Annotated[str, Security(get_id)],
    file_id: int,
):
    try:
        knowledge_id = supabase.table("file").select("knowledge_id").match({"id" : file_id}).execute().dict()["data"][0]["knowledge_id"]
        res = supabase.table("knowledge").select("*").match({"user_id" : id,"id":knowledge_id}).execute().dict()["data"]    
    except:
        raise NOT_FOUND
    if res ==[]:
        raise NOT_FOUND
    
    try:
        url = await get_link(supabase, id, file_id)
        url = url["signedURL"]
        
        embedding_file_gpt(supabase,url,file_id,knowledge_id)
        return {"detail": "File embeded"}
    except:
        raise BAD_REQUEST
    

@router.get("/get_embed", )
async def get_embed_file(
    supabase: Annotated[Client, Depends(get_supabase)],
    id: Annotated[str, Security(get_id)],
    file_id: int,
):
    try:
        knowledge_id = supabase.table("file").select("knowledge_id").match({"id" : file_id}).execute().dict()["data"][0]["knowledge_id"]
        res = supabase.table("knowledge").select("*").match({"user_id" : id,"id":knowledge_id}).execute().dict()["data"]    
    except:
        raise NOT_FOUND
    if res ==[]:
        raise NOT_FOUND
    
    try:
        res = supabase.table("documents").select("content").match({"file_id" : file_id}).execute()
        return res
    except:
        raise BAD_REQUEST

# get url of file from supabase storage
@router.get("/link", description="Get url of file")
async def get_link(
    supabase: Annotated[Client, Depends(get_supabase)],
    user_id: Annotated[str, Security(get_id)],
    file_id: int,
):
    try:
        knowledge_id = supabase.table("file").select("knowledge_id").match({"id" : file_id}).execute().dict()["data"][0]["knowledge_id"]
        res = supabase.table("knowledge").select("*").match({"user_id" : user_id,"id":knowledge_id}).execute().dict()["data"]    
    except:
        raise NOT_FOUND
    if res ==[]:
        raise NOT_FOUND
    try:
        res = supabase.storage.from_("file").create_signed_url(
            path=str(file_id), expires_in=3600
        )
        return res
    except:
        raise BAD_REQUEST
    


# delete file
@router.delete("", description="Delete file")
async def delete_file(
    supabase: Annotated[Client, Depends(get_supabase)],
    user_id: Annotated[str, Security(get_id)],
    file_id: int,
):
    knowledge_id = supabase.table("file").select("knowledge_id").match({"id" : file_id}).execute().dict()["data"][0]["knowledge_id"]
    res = supabase.table("knowledge").select("*").match({"user_id" : user_id,"id":knowledge_id}).execute().dict()["data"]    
    if res ==[]:
        raise NOT_FOUND
    
    try:
        supabase.storage.from_("file").remove([str(file_id)])
        supabase.table("file").delete().eq("id", file_id).execute()
        return {"detail": "File deleted"}
    except:
        raise BAD_REQUEST