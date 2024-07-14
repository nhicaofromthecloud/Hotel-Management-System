# src/admin.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.utils.db import get_db
from src.models.user import User
from src.models.booking import Booking
from src.models.roomtype import RoomType
from src.models.service import Service
from src.models.servicerequest import ServiceRequest

def add_user(full_name: str, email: str, password: str, role: str):
    db: Session = next(get_db())
    new_user = User(full_name=full_name, email=email, password=password, role=role)
    db.add(new_user)
    try:
        db.commit()
        print(f"User {full_name} added successfully.")
    except IntegrityError:
        db.rollback()
        print(f"Error: User with email {email} already exists.")
    finally:
        db.close()

def remove_user(user_id: int):
    db: Session = next(get_db())
    user = db.query(User).filter(User.user_id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        print(f"User {user.full_name} removed successfully.")
    else:
        print(f"User with ID {user_id} not found.")
    db.close()

def update_user(user_id: int, full_name: str = None, email: str = None, password: str = None, role: str = None):
    db: Session = next(get_db())
    user = db.query(User).filter(User.user_id == user_id).first()
    if user:
        if full_name:
            user.full_name = full_name
        if email:
            user.email = email
        if password:
            user.password = password
        if role:
            user.role = role
        db.commit()
        print(f"User {user.full_name} updated successfully.")
    else:
        print(f"User with ID {user_id} not found.")
    db.close()

def view_all_bookings():
    db: Session = next(get_db())
    bookings = db.query(Booking).all()
    for booking in bookings:
        print(f"Booking ID: {booking.booking_id}, Customer: {booking.customer_name}, Room: {booking.room_number}, Status: {booking.booking_status}")
    db.close()

def generate_financial_reports():
    db: Session = next(get_db())
    total_revenue = 0

    bookings = db.query(Booking).all()
    for booking in bookings:
        room_type = db.query(RoomType).filter(RoomType.room_type_id == booking.room_type).first()
        if room_type:
            total_revenue += room_type.fee_per_hour

    services = db.query(ServiceRequest).all()
    for service_request in services:
        service = db.query(Service).filter(Service.service_id == service_request.service_id).first()
        if service:
            total_revenue += service.service_fee

    print(f"Total Revenue: ${total_revenue}")
    db.close()
