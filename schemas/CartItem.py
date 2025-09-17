from pydantic import BaseModel

class CartItemBase(BaseModel):
    cart_id: int
    product_detail_id: int
    quantity: int

class CartItemCreate (CartItemBase):
    pass

class CartItemUpdate(BaseModel):
    cart_id: int | None = None
    product_detail_id: int | None = None
    quantity: int | None = None

class CartItemRead(CartItemBase):
    id: int

    Model_config = {
        "from_attributes": True
    }