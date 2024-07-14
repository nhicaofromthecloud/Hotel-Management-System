# src/staff.py
from sqlalchemy.orm import Session
from datetime import datetime
from src.utils.db import get_db
from src.models.booking import Booking
from src.models.room import Room
from src.models.servicerequest import ServiceRequest

def check_in(booking_id: int):
    db: Session = next(get_db())
    booking = db.query(Booking).filter(Booking.booking_id == booking_id).first()
    if booking:
        booking.checkin_time = datetime.now()
        booking.booking_status = 'Checked In'
        room = db.query(Room).filter(Room.room_number == booking.room_number).first()
        if room:
            room.room_status = 'Occupied'
        db.commit()
        print(f"Booking ID {booking_id} checked in successfully.")
    else:
        print(f"Booking ID {booking_id} not found.")
    db.close()

def check_out(booking_id: int):
    db: Session = next(get_db())
    booking = db.query(Booking).filter(Booking.booking_id == booking_id).first()
    if booking:
        booking.checkout_time = datetime.now()
        booking.booking_status = 'Checked Out'
        room = db.query(Room).filter(Room.room_number == booking.room_number).first()
        if room:
            room.room_status = 'Available'
        db.commit()
        print(f"Booking ID {booking_id} checked out successfully.")
    else:
        print(f"Booking ID {booking_id} not found.")
    db.close()

def provide_room_service(booking_id: int, service_id: int):
    db: Session = next(get_db())
    service_request = ServiceRequest(
        request_time = datetime.now(),
        booking_id = booking_id,
        service_id = service_id,
        service_status = 'Requested'
    )
    db.add(service_request)
    db.commit()
    print(f"Room service requested successfully for Booking ID {booking_id}.")
    db.close()

def update_room_status(room_number: int, status: str):
    db: Session = next(get_db())
    room = db.query(Room).filter(Room.room_number == room_number).first()
    if room:
        room.room_status = status
        db.commit()
        print(f"Room Number {room_number} status updated to {status}.")
    else:
        print(f"Room Number {room_number} not found.")
    db.close()
