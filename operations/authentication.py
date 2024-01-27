import csv
from utils.utils import csv_to_dict, user_csv_to_dict
from operations.view import guest_menu
from utils.utils import csv_to_dict


def login():
    user_data = csv_to_dict("data//guest_data.csv", "guest_email")
    email = input("Please enter your email: ").strip()
    if email in user_data:
        password = input("Please enter your password: ")
        if password == user_data[email]["password"]:
            print(f"Login successful! Welcome {user_data[email]['guest_first_name']}.")
            guest_menu(email)
        else:
            print("Incorrect password. Please try again.")
    else:
        print("Email not found. Please register or try again.")
        

def register():
    """ Function for registering the users into the system. """
    print("\nWelcome to registration page!")
    filepath = "./data/guest_data.csv"

    user_tmp = user_csv_to_dict(filepath)
 
    name = input("Write your name: ").strip()
    surname = input("Write your surname: ").strip()

    age = input("What is your age? ").strip()
    
    while not age.isdigit() or int(age) <= 0:
        age = input("Please enter a valid age (a number greater than 0): ").strip()

    email = input("Write your email: ").strip()
    while email in user_tmp:
        email = input("Email already exists. Write a new one: ").strip()


    password = input("Write a password: ")

    while ' ' in password or len(password) < 3:
        if ' ' in password:
            password = input("Password should not contain white spaces. Write a password: ")
        else:
            password = input("Password should be at least 3 characters long. Write a password: ")


    max_rid = 0
    for k, v in user_tmp.items():
        max_rid = max(max_rid,int(v['guest_id'])) 
        
    data = {
        "guest_id": max_rid+1,
        "guest_first_name": name,
        "guest_last_name": surname,
        "guest_email":email,
        "guest_age": age,
        "password":password
    }

    with open(filepath, 'a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        writer.writerow(data)
        
    print("You have successfully registered in the system.")
