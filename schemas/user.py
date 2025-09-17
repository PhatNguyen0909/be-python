from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None  # Python 3.13 hỗ trợ | None

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    full_name: str | None = None
    password: str | None = None

class UserRead(UserBase):
    id: int

    model_config = {
        "from_attributes": True  # dùng Pydantic v2
    }
