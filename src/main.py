# src/main.py   new comment trying to push from cloud9
import sys
import os
from datetime import datetime

# Add the parent directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils.db import engine, Base
import src.models  # Import all models
from src.admin import add_user, remove_user, update_user, view_all_bookings, generate_financial_reports
from src.manager import approve_booking, reject_booking, view_room_availability, generate_daily_activity_report
from src.staff import check_in, check_out, provide_room_service, update_room_status
from src.customer import book_room, check_room_availability, request_room_service

def init_db():
    print("Initializing database...")
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully!")

def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Add User")
        print("2. Remove User")
        print("3. Update User")
        print("4. View All Bookings")
        print("5. Generate Financial Reports")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            full_name = input("Full Name: ")
            email = input("Email: ")
            password = input("Password: ")
            role = input("Role: ")
            add_user(full_name, email, password, role)
        elif choice == '2':
            user_id = int(input("User ID: "))
            remove_user(user_id)
        elif choice == '3':
            user_id = int(input("User ID: "))
            full_name = input("Full Name (leave blank to skip): ")
            email = input("Email (leave blank to skip): ")
            password = input("Password (leave blank to skip): ")
            role = input("Role (leave blank to skip): ")
            update_user(user_id, full_name, email, password, role)
        elif choice == '4':
            view_all_bookings()
        elif choice == '5':
            generate_financial_reports()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def manager_menu():
    while True:
        print("\nManager Menu:")
        print("1. Approve Booking")
        print("2. Reject Booking")
        print("3. View Room Availability")
        print("4. Generate Daily Activity Report")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            booking_id = int(input("Booking ID: "))
            approve_booking(booking_id)
        elif choice == '2':
            booking_id = int(input("Booking ID: "))
            reject_booking(booking_id)
        elif choice == '3':
            view_room_availability()
        elif choice == '4':
            generate_daily_activity_report()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def staff_menu():
    while True:
        print("\nStaff Menu:")
        print("1. Check In")
        print("2. Check Out")
        print("3. Provide Room Service")
        print("4. Update Room Status")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            booking_id = int(input("Booking ID: "))
            check_in(booking_id)
        elif choice == '2':
            booking_id = int(input("Booking ID: "))
            check_out(booking_id)
        elif choice == '3':
            booking_id = int(input("Booking ID: "))
            service_id = int(input("Service ID: "))
            provide_room_service(booking_id, service_id)
        elif choice == '4':
            room_number = int(input("Room Number: "))
            status = input("Status: ")
            update_room_status(room_number, status)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def customer_menu():
    while True:
        print("\nCustomer Menu:")
        print("1. Book Room")
        print("2. Check Room Availability")
        print("3. Request Room Service")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            customer_id = int(input("Customer ID: "))
            customer_name = input("Customer Name: ")
            room_number = int(input("Room Number: "))
            checkin_time = datetime.strptime(input("Check-in Time (YYYY-MM-DD HH:MM:SS): "), '%Y-%m-%d %H:%M:%S')
            checkout_time = datetime.strptime(input("Check-out Time (YYYY-MM-DD HH:MM:SS): "), '%Y-%m-%d %H:%M:%S')
            book_room(customer_id, customer_name, room_number, checkin_time, checkout_time)
        elif choice == '2':
            room_number = int(input("Room Number: "))
            check_room_availability(room_number)
        elif choice == '3':
            booking_id = int(input("Booking ID: "))
            service_id = int(input("Service ID: "))
            request_room_service(booking_id, service_id)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    init_db()
    while True:
        print("\nMain Menu:")
        print("1. Admin")
        print("2. Manager")
        print("3. Staff")
        print("4. Customer")
        print("5. Exit")
        choice = input("Select a role: ")

        if choice == '1':
            admin_menu()
        elif choice == '2':
            manager_menu()
        elif choice == '3':
            staff_menu()
        elif choice == '4':
            customer_menu()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
