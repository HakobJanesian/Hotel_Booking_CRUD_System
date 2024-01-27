# Hotel Booking System

The Hotel Booking System is a comprehensive console-based application designed to manage hotel reservations efficiently. This documentation aims to guide users through its functionalities, providing an understanding of its operations and code structure.

## Features

### User Authentication
`operations/authentication.py`

- **Login**
  - Users can log in using their email and password.
  - Successful login redirects to the guest menu.

- **Registration**
  - New users can register by providing their name, surname, age, email, and password.
  - Ensures email uniqueness and password length (minimum 3 characters).

### Guest Menu and Operations
`view.py`

- **Review Active Bookings**
  - Displays a list of active bookings linked to the user's email.

- **Make Booking**
  - Create new bookings by selecting a country (via country code), hotel (via hotel ID), check-in and check-out dates, number of adults and children, and room type.
  - Verifies that the check-out date is later than the check-in date.

- **Cancel Booking**
  - Allows users to cancel a booking using the booking ID.

### CRUD Operations
`crud.py`

- **Data Retrieval**
  - Fetch active bookings for a specific user email from booking data.

- **Data Modification**
  - Create new bookings and cancel existing ones in `booking_data.csv`.

### Validation Checks
`validation.py`

- **Room Type**
  - Validates the room type against a predefined list.

- **Country Code**
  - Checks if the entered country code is valid.

- **Check-in and Check-out Dates**
  - Ensures the check-in date is before the check-out date.

### Utility Functions
`utils/utils.py`

- **CSV to Dictionary Conversion**
  - Converts CSV files into dictionaries for easy data manipulation.

- **Writing Data to CSV**
  - Updates CSV files with new or modified data.

## Code Snippets and Function Descriptions

### Authentication (`operations/authentication.py`)
- `login()`: Checks user credentials against `guest_data.csv` and logs in if valid.
- `register()`: Adds new user details to `guest_data.csv`.

### Guest Menu and Booking Operations (`view.py`)
- `guest_menu(email)`: Displays options for the logged-in user.
- `review_active_bookings(email)`: Retrieves and displays active bookings.
- `make_booking(guest_email)`: Guides through creating a new booking.
- `cancel_booking()`: Cancels an existing booking by booking ID.
- `select_option(options, prompt)`: Presents options and captures user selection.

### CRUD Operations (`crud.py`)
- `get_active_bookings(guest_email, bookings_data)`: Fetches active bookings.
- `create_booking(booking_data, bookings_filepath)`: Adds new booking.
- `cancel_booking_helper(booking_id, bookings_filepath)`: Cancels a booking.

### Validation Checks (`validation.py`)
- `check_room_type(room_type)`: Validates room type.
- `check_country_code(code)`: Verifies country code.
- `check_country_name(name)`: Checks country name.
- `validate_check_in_out_dates(check_in, check_out)`: Validates dates.

### Utility Functions (`utils/utils.py`)
- `csv_to_dict(filepath, key_field)`: Converts CSV to dictionary.
- `transform_csv_to_dict(filepath, key_field)`: Transforms booking data.
- `write_dict_to_csv(filepath, data)`: Writes data back to CSV.
- `user_csv_to_dict(filepath)`: Reads guest data and converts to dictionary.

### Entry Point
`main.py`

- `main()`: Initial menu for login, registration, or exit.

## Additional Details

- **Country and Hotel Selection**
  - Enter country code and hotel ID for booking.

- **Date-Validation**
  - System checks that check-out date is later than check-in date.

- **User Registration**
  - Requires a unique email and a password of at least 3 characters.
