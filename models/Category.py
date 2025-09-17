from sqlalchemy import Column, Integer, String
from core.db import Base

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True, index=True)
    description = Column(String(255))
