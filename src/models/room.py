# src/models/room.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.utils.db import Base

class Room(Base):
    __tablename__ = 'rooms'

    room_number = Column(Integer, primary_key=True, index=True)
    room_type = Column(Integer, ForeignKey('roomtypes.room_type_id'))
    number_of_beds = Column(Integer, nullable=False)
    room_status = Column(String(20), nullable=False)

    roomtype = relationship("RoomType", back_populates="rooms")

    def __repr__(self):
        return f'<Room {self.room_number}>'
