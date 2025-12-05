from pydantic import BaseModel, EmailStr
from typing import Optional, List


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    is_active: bool


class Config:
    orm_mode = True


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None


class TaskCreate(TaskBase):
    pass


class TaskOut(TaskBase):
    id: int
    completed: bool
    owner_id: Optional[int]


class Config:
    orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"