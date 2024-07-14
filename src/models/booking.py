# src/models/booking.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.utils.db import Base

class Booking(Base):
    __tablename__ = 'bookings'

    booking_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey('users.user_id'))
    customer_name = Column(String(100), nullable=False)
    room_number = Column(Integer, ForeignKey('rooms.room_number'))
    booking_status = Column(String(20), nullable=False)
    checkin_time = Column(DateTime, nullable=False)
    checkout_time = Column(DateTime, nullable=False)

    room = relationship("Room")
    customer = relationship("User")

    def __repr__(self):
        return f'<Booking {self.booking_id}>'
