from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from core.db import Base

class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True, index=True)
    category_id = Column(Integer, ForeignKey('category.id'))
    base_price = Column(Numeric(10,2), nullable=False)
    description = Column(String(255))

