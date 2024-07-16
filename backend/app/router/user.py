from fastapi import APIRouter, Depends, HTTPException, Security, Request, Form, File, UploadFile, status
from fastapi.encoders import jsonable_encoder
from supabase import Client
from utils.exceptions import BAD_REQUEST, FORBIDDEN, NOT_FOUND, CONFLICT
from typing import Annotated, List
from database.db_service import get_supabase
from fastapi.security import  OAuth2PasswordRequestForm
from model.user import User, UserShow
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



# @router.patch("/change_info", description="Update user info")
# async def update_user_info(
#     supabase: Annotated[Client, Depends(get_supabase)],
#     new_user_info: User,
#     token: Annotated[str, Depends(oauth2_scheme)],
    

# ):
#         session = supabase.auth.get_session()
#         user_id = supabase.auth.get_user(token).user.id
#         update_response = await supabase.auth.update_user({
#             "username": new_user_info.username
#         })
#     # try:
#         # await supabase.auth.update_user(token,{"username": new_user_info.username})
#         # return {"detail": "User info updated"}
#     # except:
#     #     raise BAD_REQUEST



# @router.patch("/update_avatar")
# async def create_upload_file(
#     file: UploadFile,
#     user_id: int,
#     supabase: Annotated[Client, Depends(get_supabase)]
# ):  
#     try:
#         user  = supabase.table("user").select("*").eq("id", user_id).execute().data[0]
#         if not user:
#             return NOT_FOUND
            
#         f = await file.read()

#         if user["avatar"] == "https://i.sstatic.net/l60Hf.png":
#             supabase.storage.from_("avatar").upload(
#             path=f'avatar_{user_id}', file=f, file_options={"content-type": "image/jpeg"}
#             )
#         else:
#             supabase.storage.from_("avatar").update(
#             path=f'avatar_{user_id}', file=f, file_options={"content-type": "image/jpeg"}
#             )

#         url = supabase.storage.from_('avatar').create_signed_url(path=f'avatar_{user_id}', expires_in=30000000)
            
#         supabase.table("user").update({"avatar": url}).eq("id", user_id).execute()

#         return {"detail": "successfully uploaded avatar"}
#     except:
#         return BAD_REQUEST

