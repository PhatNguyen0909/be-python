from sqlalchemy import Column, Integer, ForeignKey, Numeric
from core.db import Base

class CartItem(Base):
    __tablename__ = 'cart_item'

    id = Column(Integer, primary_key=True)
    cart_id = Column(Integer, ForeignKey('cart.id'), nullable=False, index=True)
    product_detail_id = Column(Integer, ForeignKey('product_detail.id'), nullable=False, index=True)
    quantity = Column(Integer, nullable=False, default=1)