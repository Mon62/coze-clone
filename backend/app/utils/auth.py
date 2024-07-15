from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from database.db_service import get_supabase
from supabase import Client
from utils.exceptions import BAD_REQUEST, UNAUTHORIZED

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_user_response(token: str, supabase: Client):
    try:
        return supabase.auth.get_user(token)
    except:
        raise BAD_REQUEST


async def get_id(
    token: Annotated[str, Depends(oauth2_scheme)],
    supabase: Annotated[Client, Depends(get_supabase)],
):
    try:
        res = get_user_response(token, supabase)
        if res is None:
            raise UNAUTHORIZED
        id: str = res.user.id
        return id
    except:
        raise UNAUTHORIZED
