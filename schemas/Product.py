from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    category_id : int
    base_price: float
    description : str
class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    name: str | None = None
    category_id : int | None = None
    base_price: float | None = None
    description : str | None = None

class ProductRead(ProductBase):
    id: int

    model_config = {
        "from_attributes": True  # dùng Pydantic v2
    }
