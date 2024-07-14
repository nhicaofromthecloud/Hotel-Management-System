# src/models/roomtype.py
from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from src.utils.db import Base

class RoomType(Base):
    __tablename__ = 'roomtypes'

    room_type_id = Column(Integer, primary_key=True, index=True)
    room_type_name = Column(String(100), nullable=False)
    fee_per_hour = Column(DECIMAL(6, 2), nullable=False)

    rooms = relationship("Room", back_populates="roomtype")

    def __repr__(self):
        return f'<RoomType {self.room_type_name}>'
