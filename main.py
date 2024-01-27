import warnings
warnings.filterwarnings("ignore")

from operations.authentication import login, register

def main():
    print("Welcome to the Hotel Booking System!")
    while True:
        user_input = input("Please enter an operation (login: 1, register: 2, exit: 0): ").strip()
        if user_input == "1":
            login()
        elif user_input == "2":
            register()
        elif user_input == "0":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid input! Please choose a valid operation.")

if __name__ == "__main__":
    main()
