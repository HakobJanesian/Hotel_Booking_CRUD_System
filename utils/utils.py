import csv


def csv_to_dict(filepath, key_field):
    data = dict()
    with open(filepath, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                data[row[key_field]] = row
            except KeyError:
                print(f"Warning: Key '{key_field}' not found in row: {row}")
    return data


def transform_csv_to_dict(filepath, key_field):
    result_dict = {}
    try:
        with open(filepath, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    result_dict[row[key_field]] = row
                except KeyError:
                    pass
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return result_dict


def write_dict_to_csv(filepath, data):
    if data:
        fieldnames = next(iter(data.values())).keys()
        with open(filepath, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in data.values():
                writer.writerow(row)
    return None


def user_csv_to_dict(filepath):
    """ Function to read user's data file into a dictionary. """
    user_data = dict()

    with open(filepath) as user_data_file:
        user_data_reader = csv.DictReader(user_data_file)

        for row in user_data_reader:

            user_data[row["guest_email"]] = {key:value for key,value in row.items() if key != "guest_email"}

    return user_data
