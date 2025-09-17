from pydantic import BaseModel



class ProductDetailBase(BaseModel):
    ProductID: int
    size: str
    color: str
    stock : int
    price: float | None = None

class ProductDetailCreate(ProductDetailBase):
    pass

class ProductDetailUpdate(BaseModel):
    size: str | None = None
    color: str | None = None
    stock: int | None = None
    price: float | None = None

class ProductDetailRead (ProductDetailBase):
    id: int

    model_config = {
        "from_attributes": True
    }