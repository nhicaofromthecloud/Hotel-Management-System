# src/models/service.py
from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from src.utils.db import Base

class Service(Base):
    __tablename__ = 'services'

    service_id = Column(Integer, primary_key=True, index=True)
    service_name = Column(String(100), nullable=False)
    service_fee = Column(DECIMAL(6, 2), nullable=False)

    servicerequests = relationship("ServiceRequest", back_populates="service")

    def __repr__(self):
        return f'<Service {self.service_name}>'
