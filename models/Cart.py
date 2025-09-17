from sqlalchemy import Column, Integer, ForeignKey, Numeric
from core.db import Base

class Cart(Base):
    __tablename__ = 'cart'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False, index=True)  # liên kết người dùng, giả sử có bảng User
    total_amount = Column(Numeric(10,2), nullable=False, default=0)
