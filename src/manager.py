# src/manager.py
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from src.utils.db import get_db
from src.models.booking import Booking
from src.models.room import Room
from src.models.servicerequest import ServiceRequest

def approve_booking(booking_id: int):
    db: Session = next(get_db())
    booking = db.query(Booking).filter(Booking.booking_id == booking_id).first()
    if booking:
        booking.booking_status = 'Approved'
        db.commit()
        print(f"Booking ID {booking_id} approved successfully.")
    else:
        print(f"Booking ID {booking_id} not found.")
    db.close()

def reject_booking(booking_id: int):
    db: Session = next(get_db())
    booking = db.query(Booking).filter(Booking.booking_id == booking_id).first()
    if booking:
        booking.booking_status = 'Rejected'
        db.commit()
        print(f"Booking ID {booking_id} rejected successfully.")
    else:
        print(f"Booking ID {booking_id} not found.")
    db.close()

def view_room_availability():
    db: Session = next(get_db())
    rooms = db.query(Room).all()
    for room in rooms:
        print(f"Room Number: {room.room_number}, Status: {room.room_status}")
    db.close()

def generate_daily_activity_report():
    db: Session = next(get_db())
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    
    bookings = db.query(Booking).filter(Booking.checkin_time >= yesterday, Booking.checkin_time < today).all()
    services = db.query(ServiceRequest).filter(ServiceRequest.request_time >= yesterday, ServiceRequest.request_time < today).all()

    print("Daily Activity Report:")
    print("\nBookings:")
    for booking in bookings:
        print(f"Booking ID: {booking.booking_id}, Customer: {booking.customer_name}, Room: {booking.room_number}, Status: {booking.booking_status}")

    print("\nService Requests:")
    for service in services:
        print(f"Service Request ID: {service.request_id}, Booking ID: {service.booking_id}, Service: {service.service_id}, Status: {service.service_status}")

    db.close()
