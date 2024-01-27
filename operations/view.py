from operations.validation import check_country_code, check_room_type, validate_check_in_out_dates
from utils.utils import csv_to_dict, transform_csv_to_dict
from .crud import create_booking, cancel_booking_helper, get_active_bookings, get_selection_options

from datetime import datetime


def guest_menu(email):
    print(f"Welcome to the Guest Menu, {email}")
    while True:
        choice = input("1. Review Active Bookings\n2. Make Booking\n3. Cancel Booking\n4. Logout\nEnter choice (1, 2, 3 or 4): ").strip()
        if choice == "1":
            review_active_bookings(email)
        elif choice == "2":
            make_booking(email)
        elif choice == "3":
            cancel_booking(email)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

         
def review_active_bookings(email):
    bookings_data = transform_csv_to_dict('data/booking_data.csv', 'booking_id')
    active_bookings = get_active_bookings(email, bookings_data)
    if active_bookings:
        for booking in active_bookings:
            check_in = datetime.strptime(booking['check_in'], '%d/%m/%Y').strftime('%d/%m/%Y')
            check_out = datetime.strptime(booking['check_out'], '%d/%m/%Y').strftime('%d/%m/%Y')

            print(f"Booking ID: {booking['booking_id']}, Hotel ID: {booking['hotel_name']}, Check-In: {check_in}, Check-Out: {check_out}, Room Type: {booking['room_type']}")
    else:
        print("No active bookings found.")
    input("Press Enter to return to the menu.")
    

from datetime import datetime

def make_booking(guest_email):

    countries_data = csv_to_dict('data/country_data.csv', 'country_code')
    countries = get_selection_options(countries_data, 'country_code', 'country_name')
    country_code = select_option(countries, "Select Country: ")
    country_name = countries_data[country_code]['country_name']
    
    bookings_data = csv_to_dict('data/booking_data.csv', 'booking_id')
    valid_booking_ids = [int(booking_id) for booking_id in bookings_data.keys() if booking_id.isdigit()]
    max_booking_id = max(valid_booking_ids) if valid_booking_ids else 0

    hotels_data = csv_to_dict('data/hotel_data.csv', 'hotel_id')
    hotels = {hotel_id: hotel['hotel_name'] for hotel_id, hotel in hotels_data.items() if hotel['country_code'] == country_code}
    hotel_id = select_option(hotels, "Select Hotel: ")
    hotel_name = hotels[hotel_id]

    def validate_date(date_string):
        try:
            if '-' in date_string:
                datetime.strptime(date_string.strip(), '%Y-%m-%d')
            else:
                datetime.strptime(date_string.strip(), '%d/%m/%Y')
            return True
        except ValueError:
            return False


    check_in = input("Enter Check-In Date (YYYY-MM-DD): ").strip()
    while not validate_date(check_in):
        print("Invalid date format! Please use YYYY-MM-DD.")
        check_in = input("Enter Check-In Date (YYYY-MM-DD): ").strip()

    check_out = input("Enter Check-Out Date (YYYY-MM-DD): ").strip()
    while not validate_date(check_out):
        print("Invalid date format! Please use YYYY-MM-DD.")
        check_out = input("Enter Check-Out Date (YYYY-MM-DD): ").strip()

    # Format the dates to 'D/M/YYYY' before saving to CSV
    check_in_formatted = datetime.strptime(check_in, '%Y-%m-%d').strftime('%d/%m/%Y')
    check_out_formatted = datetime.strptime(check_out, '%Y-%m-%d').strftime('%d/%m/%Y')

    adults = input("Enter number of adults: ")
    children = input("Enter number of children: ")

    print(f"Select from the given list of options:\nSingle, Double, Triple\nQuad, Queen, King, Twin")
    room_type = input("Enter Room Type: ")

    if check_room_type(str(room_type)) and int(adults) >= 1 and int(children) >= 0 and check_country_code(int(country_code)) and  validate_check_in_out_dates(check_in, check_out):
        booking_data = {
            "booking_id": max_booking_id + 1, 
            "user_email": guest_email,
            "country_name": country_name,
            "hotel_name": hotel_name,
            "adults": int(adults),
            "children": int(children),
            "status": "active",
            "check_in": check_in_formatted,
            "check_out": check_out_formatted,
            "room_type": room_type.lower()
        }
        
        create_booking(booking_data, 'data/booking_data.csv')  
        print("Booking created successfully.")
        input("Press Enter to return to the menu.")
    else:
        print("Unable to create booking. Please ensure all inputs are valid.")


def cancel_booking(email):
    bookings_data = transform_csv_to_dict('data/booking_data.csv', 'booking_id')
    user_active_bookings = get_active_bookings(email, bookings_data)

    if not user_active_bookings:
        print("You do not have any active bookings to cancel.")
        input("Press Enter to return to the menu.")
        return

    booking_id = input("Enter Booking ID to cancel: ").strip()

    if booking_id in bookings_data and bookings_data[booking_id]['guest_email'] == email:
        if bookings_data[booking_id]['status'] == 'active':
            if cancel_booking_helper(booking_id, 'data/booking_data.csv'):  
                print("Booking cancelled successfully.")
            else:
                print("Unable to cancel the booking.")
        else:
            print("This booking is already cancelled.")
    else:
        print("Booking ID not found or it does not belong to you.")

    input("Press Enter to return to the menu.")




def select_option(options, prompt):
    while True:
        print(prompt)
        for key, value in options.items():
            print(f"{key}: {value}")
        selection = input("Select from the above-given options (enter the key): ")
        selection = selection.strip()
        if selection in options:
            return selection
        else:
            print("Invalid selection. Please try again.")
