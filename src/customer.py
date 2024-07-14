# src/customer.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from src.utils.db import get_db
from src.models.booking import Booking
from src.models.room import Room

def book_room(customer_id: int, customer_name: str, room_number: int, checkin_time: datetime, checkout_time: datetime):
    db: Session = next(get_db())
    new_booking = Booking(
        customer_id=customer_id,
        customer_name=customer_name,
        room_number=room_number,
        checkin_time=checkin_time,
        checkout_time=checkout_time,
        booking_status='Pending'
    )
    room = db.query(Room).filter(Room.room_number == room_number).first()
    if room and room.room_status == 'Available':
        db.add(new_booking)
        try:
            db.commit()
            print(f"Room {room_number} booked successfully for {customer_name}.")
        except IntegrityError as e:
            db.rollback()
            print(f"Error: Booking for room {room_number} could not be completed. IntegrityError: {e.orig}")
        except Exception as e:
            db.rollback()
            print(f"Error: Booking for room {room_number} could not be completed. Exception: {e}")
    else:
        print(f"Room {room_number} is not available.")
    db.close()


def check_room_availability(room_number: int):
    db: Session = next(get_db())
    room = db.query(Room).filter(Room.room_number == room_number).first()
    if room:
        print(f"Room Number: {room.room_number}, Status: {room.room_status}")
    else:
        print(f"Room Number {room_number} not found.")
    db.close()

def request_room_service(booking_id: int, service_id: int):
    db: Session = next(get_db())
    service_request = ServiceRequest(
        request_time=datetime.now(),
        booking_id=booking_id,
        service_id=service_id,
        service_status='Requested'
    )
    db.add(service_request)
    db.commit()
    print(f"Room service requested successfully for Booking ID {booking_id}.")
    db.close()
