from datetime import datetime

unique_room_types = [
    "Single", "Double", "Triple", "Quad", "Queen", "King", "Twin"
]

def check_room_type(room_type, unique_room_types=unique_room_types):
    lower_unique_room_types = [rt.lower() for rt in unique_room_types]

    if isinstance(room_type, str):
        return room_type.lower() in lower_unique_room_types
    elif isinstance(room_type, list):
        return [single_room_type.lower() in lower_unique_room_types for single_room_type in room_type]
    else:
        raise ValueError("Input must be a string or a list of strings.")


unique_country_codes = [
    512, 705, 392, 492, 300, 364, 528, 634, 380, 604
]

def check_country_code(code, unique_country_codes=unique_country_codes):
    if isinstance(code, int):
        return code in unique_country_codes
    elif isinstance(code, list):
        return [single_code in unique_country_codes for single_code in code]
    else:
        raise ValueError("Input must be an integer or a list of integers.")

unique_country_names = [
    "Greece", "Iran", "Italy", "Japan", "Monaco", "Oman", "Netherlands", "Peru", "Qatar", "Slovenia"
]

def check_country_name(name, unique_country_names=unique_country_names):
    if isinstance(name, str):
        return name in unique_country_names
    elif isinstance(name, list):
        return [single_name in unique_country_names for single_name in name]
    else:
        raise ValueError("Input must be a string or a list of strings.")

    
def validate_check_in_out_dates(check_in, check_out):
    try:
        check_in_date = datetime.strptime(check_in.strip(), '%Y-%m-%d')
        check_out_date = datetime.strptime(check_out.strip(), '%Y-%m-%d')

        if check_in_date < check_out_date:
            return True
        else:
            print("Check-out date must be after the check-in date.")
            return False
    except ValueError:
        print("Invalid input, check-in or check-out date should be valid!")
        return False

