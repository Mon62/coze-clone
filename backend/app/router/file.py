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
async def upload_and_embedding_file(
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
        unique_filename = str(uuid.uuid4()) + '_' + file.filename
        f = await file.read()
        supabase.storage.from_("file").upload(
            path= unique_filename, file=f, file_options={"content-type": "application/pdf"}
        )
        res = supabase.table("file").insert(
            {"name": file.filename, "name_in_storage": unique_filename,"knowledge_id":knowledge_id}
        ).execute()
        file_id = res.data[0]['id']
        if "gpt" in res[0]['embed_model']:
            url = await get_link(supabase, id, unique_filename)
            url = url["signedURL"]
            embedding_file_gpt(supabase,url,file_id,knowledge_id)
        elif "gemini" in res[0]['embed_model']:
            pass
        else:
            raise BAD_REQUEST

        return {"detail": "File uploaded"}
    except:
        raise BAD_REQUEST
    


# get url of file from supabase storage
@router.get("/link", description="Get url of file")
async def get_link(
    supabase: Annotated[Client, Depends(get_supabase)],
    user_id: Annotated[str, Security(get_id)],
    name_in_storage: str,
):
    knowledge_id = supabase.table("file").select("knowledge_id").match({"name_in_storage" : name_in_storage}).execute().dict()["data"][0]["knowledge_id"]
    res = supabase.table("knowledge").select("*").match({"user_id" : user_id,"id":knowledge_id}).execute().dict()["data"]    
    if res ==[]:
        raise NOT_FOUND
    try:
        res = supabase.storage.from_("file").create_signed_url(
            path=name_in_storage, expires_in=3600
        )
        return res
    except:
        raise 
    


# delete file
@router.delete("", description="Delete file")
async def delete_file(
    supabase: Annotated[Client, Depends(get_supabase)],
    user_id: Annotated[str, Security(get_id)],
    name_in_storage: str,
):
    knowledge_id = supabase.table("file").select("knowledge_id").match({"name_in_storage" : name_in_storage}).execute().dict()["data"][0]["knowledge_id"]
    res = supabase.table("knowledge").select("*").match({"user_id" : user_id,"id":knowledge_id}).execute().dict()["data"]    
    if res ==[]:
        raise NOT_FOUND
    
    try:
        supabase.storage.from_("file").remove([name_in_storage])
        supabase.table("file").delete().eq("name_in_storage", name_in_storage).execute()
        return {"detail": "File deleted"}
    except:
        raise BAD_REQUEST