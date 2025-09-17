from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from core.db import Base


class ProductDetail(Base):
    __tablename__ = 'product_detail'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False, index=True)
    size = Column(String(10), nullable=False)
    color = Column(String(30), nullable=False)
    stock = Column(Integer, nullable=False, default=0)
    price = Column(Numeric(10,2), nullable=False)
    sku = Column(String(50), unique=True, index=True)