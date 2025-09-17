from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from core.db import get_db
from schemas.user import UserCreate, UserRead, UserUpdate
from services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])

def get_user_service(db: Session = Depends(get_db)):
    return UserService(db)

@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, svc: UserService = Depends(get_user_service)):
    try:
        return svc.create_user(user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[UserRead])
def list_users(svc: UserService = Depends(get_user_service)):
    return svc.list_users()

@router.patch("/{user_id}", response_model=UserRead)
def update_user(user_id: int, updates: UserUpdate, svc: UserService = Depends(get_user_service)):
    try:
        return svc.update_user(user_id, updates)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{user_id}")
def delete_user(user_id: int, svc: UserService = Depends(get_user_service)):
    try:
        return svc.delete_user(user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
