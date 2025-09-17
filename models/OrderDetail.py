from sqlalchemy import Column, Integer, ForeignKey, Numeric, DateTime, String
from sqlalchemy.sql import func
from core.db import Base

class OrderDetail(Base):
    __tablename__ = 'order_detail'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False, index=True)
    product_detail_id = Column(Integer, ForeignKey('product_detail.id'), nullable=False, index=True)
    quantity = Column(Integer, nullable=False, default=1)
    price = Column(Numeric(10,2), nullable=False)