from fastapi import APIRouter, Depends, HTTPException, Security, Request, Form, File, UploadFile
from fastapi.encoders import jsonable_encoder
from supabase import Client
from utils.exceptions import BAD_REQUEST, FORBIDDEN, NOT_FOUND
from typing import Annotated, List
from database.db_service import get_supabase
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from model.user import User, UserLogin
from utils.auth import get_password_hash, verify_password

router = APIRouter(tags=["User"], prefix="/user")

@router.post("/register")
async def register_user(
    user: User, 
    supabase: Annotated[Client, Depends(get_supabase)]
):
    try:
        user.password = get_password_hash(user.password)
        data = jsonable_encoder(user)
        print(data)
        obj=supabase.table("user").insert(data).execute()
        print(obj)
        return {"detail": "suuccessfully registered user"}
    
    except:
        return BAD_REQUEST
    
@router.post("/login")
async def login_user(
    form_data: UserLogin,
    supabase: Annotated[Client, Depends(get_supabase)]
):
    try:
        username = form_data.username
        password = form_data.password
        user = supabase.table("user").select("*").eq("username", username).execute().data
        print (user)
        if not user:
            return NOT_FOUND
        if not verify_password(password, user[0]["password"]):
            return FORBIDDEN
        return {"detail": "successfully logged in"}
    except:
        return BAD_REQUEST
    
@router.get("/get_all_users")
async def get_all_users(
    supabase: Annotated[Client, Depends(get_supabase)]
):
    try:
        users = supabase.table("user").select("*").execute().data
        return users
    except:
        return NOT_FOUND
    
@router.patch("/update_user")
async def update_user(
    user: User,
    supabase: Annotated[Client, Depends(get_supabase)]
):
    try:
        data = jsonable_encoder(user)
        supabase.table("user").update(data).execute()
        return {"detail": "successfully updated user"}
    except:
        return BAD_REQUEST

@router.post("/uploadfile/")
async def create_upload_file(
    file: UploadFile,
    supabase: Annotated[Client, Depends(get_supabase)]
):  
    
    f = await file.read()
    supabase.storage.from_("avatar").upload(
        path=file.filename, file=f, file_options={"content-type": "image/jpeg"}
    )

    return {"filename": file.filename}