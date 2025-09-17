from pydantic import BaseModel

class CartBase(BaseModel):
    user_id: int
    total_amount: float

class CartCreate(CartBase):
    pass

class CartUpdate(BaseModel):
    user_id: int | None = None
    total_amount: float | None = None

class CartRead(CartBase):
    id: int

    Model_config = {
        "from_attributes": True
    }