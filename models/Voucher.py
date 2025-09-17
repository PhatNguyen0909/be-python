from sqlalchemy import Column, Integer, String, Numeric, DateTime, Boolean
from sqlalchemy.sql import func
from core.db import Base

class Voucher(Base):
    __tablename__ = 'voucher'

    id = Column(Integer, primary_key=True)
    code = Column(String(50), nullable=False, unique=True, index=True)
    discount_percent = Column(Numeric(5,2), nullable=False, default=0)  # giảm theo %: 10% = 10
    max_discount_amount = Column(Numeric(10,2), nullable=True)          # giảm tối đa, nếu cần
    start_date = Column(DateTime(timezone=True), nullable=False)
    end_date = Column(DateTime(timezone=True), nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
