from fastapi import APIRouter, Depends, Security, UploadFile, HTTPException, status
from supabase import Client
from utils.exceptions import BAD_REQUEST, FORBIDDEN, NOT_FOUND
from typing import Annotated, List
from database.db_service import get_supabase
from utils.auth import get_id
import uuid
from model.knowledge import File

router = APIRouter(tags=["Documents"], prefix='/documents')

