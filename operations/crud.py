import csv
from utils.utils import csv_to_dict, write_dict_to_csv, transform_csv_to_dict


def get_active_bookings(guest_email, bookings_data):
    return [booking for booking in bookings_data.values() if booking['guest_email'] == 
            guest_email and booking['status'] == 'active']


def create_booking(booking_data, bookings_filepath):
    with open(bookings_filepath, 'a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=booking_data.keys())
        file.seek(0, 2)  
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(booking_data)
        

def cancel_booking_helper(booking_id, bookings_filepath):
    bookings = transform_csv_to_dict(bookings_filepath, 'booking_id')
    if booking_id in bookings:
        bookings[booking_id]['status'] = 'cancelled'
        write_dict_to_csv(bookings_filepath, bookings)
        return True
    return False



def get_selection_options(data, key_field, display_field):
    return {item[key_field]: item[display_field] for item in data.values()}
