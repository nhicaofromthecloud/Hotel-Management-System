# src/models/servicerequest.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.utils.db import Base

class ServiceRequest(Base):
    __tablename__ = 'servicerequests'

    request_id = Column(Integer, primary_key=True, index=True)
    request_time = Column(DateTime, nullable=False)
    booking_id = Column(Integer, ForeignKey('bookings.booking_id'))
    service_id = Column(Integer, ForeignKey('services.service_id'))
    extra_notes = Column(String(100))
    service_status = Column(String(20), nullable=False)

    booking = relationship("Booking")
    service = relationship("Service", back_populates="servicerequests")

    def __repr__(self):
        return f'<ServiceRequest {self.request_id}>'
