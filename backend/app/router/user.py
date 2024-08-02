from fastapi import APIRouter, Depends, HTTPException,  status, UploadFile, Security
from fastapi.encoders import jsonable_encoder
from supabase import Client
from utils.exceptions import BAD_REQUEST, FORBIDDEN, NOT_FOUND, CONFLICT
from typing import Annotated, List
from database.db_service import get_supabase
from fastapi.security import  OAuth2PasswordRequestForm
from model.user import User, UserShow, UserUpdate
from utils.auth import get_id, oauth2_scheme, get_user_response
from gotrue.errors import AuthApiError




router = APIRouter(tags=["User"])

@router.post("/register")
async def register_user(
    user: User, 
    supabase: Annotated[Client, Depends(get_supabase)]
):
    if len(user.password) < 6:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password should be at least 6 characters",
        )
    try:
        res = supabase.auth.sign_up(
            {
                "email": user.mail,
                "password": user.password,
                "options": {
                    "data": jsonable_encoder(user, exclude=("password", "email"))
                },
            }
        )
        return {"detail": "User created"}
    except AuthApiError:
        raise CONFLICT
    except :
        return BAD_REQUEST
    

    
@router.post("/login")
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    supabase: Annotated[Client, Depends(get_supabase)],
):
    email = form_data.username
    password = form_data.password
    try:
        user = supabase.auth.sign_in_with_password(
            {"email": email, "password": password}
        )
        return {
            "access_token": user.session.access_token,
            "token_type": "bearer",
        }
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password",
        )

@router.get("/info")
async def get_user_info(
    token: Annotated[str, Depends(oauth2_scheme)],
    supabase: Annotated[Client, Depends(get_supabase)],
):
    """
    Get information of logged in user
    """
    user_response = get_user_response(token, supabase)
    return UserShow(username=user_response.user.user_metadata["username"],mail=user_response.user.user_metadata["mail"],avatar=user_response.user.user_metadata["avatar"])

@router.delete("/delete", description="Delete user")
async def update_user_info(
    supabase: Annotated[Client, Depends(get_supabase)],
    id: Annotated[str, Depends(get_id)],
):
    try:
        res = supabase.auth.admin.deleteUser(id)
        return {"detail": "successfully delete"}
    except:
        raise BAD_REQUEST


@router.patch("/change_info", description="Update user info")
async def update_user_info(
    supabase: Annotated[Client, Depends(get_supabase)],
    new_user_info: UserUpdate,
    id: Annotated[str, Depends(get_id)],
    

):
    try:
        res = supabase.auth.admin.update_user_by_id(id,{ 'user_metadata': { 'mail': new_user_info.mail,'username':new_user_info.username } })
        return {"detail": "successfully update"}
    except:
        raise BAD_REQUEST

@router.patch("/change_password")
async def change_password(
    supabase: Annotated[Client, Depends(get_supabase)],
    password:str,
    id: Annotated[str, Depends(get_id)],
):
    try:
        res = supabase.auth.admin.update_user_by_id(id,{ 'password': password })
        return {"detail": "successfully update"}
    except:
        raise BAD_REQUEST


@router.patch("/update_avatar")
async def create_upload_file(
    file: UploadFile,
    supabase: Annotated[Client, Depends(get_supabase)],
    token: str = Depends(oauth2_scheme)
):  
    if file.content_type != "image/jpeg":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only image file is accepted",
        )
    try:
        user = supabase.auth.get_user(token).user
        f = await file.read()
        if user.user_metadata['avatar'] == "https://i.sstatic.net/l60Hf.png":
            supabase.storage.from_("avatar").upload(
            path=f'avatar_{user.id}', file=f, file_options={"content-type": "image/jpeg"}
            )
        else:
            supabase.storage.from_("avatar").update(
            path=f'avatar_{user.id}', file=f, file_options={"content-type": "image/jpeg"}
            )

        url = supabase.storage.from_('avatar').create_signed_url(path=f'avatar_{user.id}', expires_in=30000000)["signedURL"]

        res = supabase.auth.admin.update_user_by_id(user.id,{ 'user_metadata': { 'avatar': url } })

        return {"detail": "successfully uploaded avatar"}
    except:
        return BAD_REQUEST

