# Initialize seat layout
seats = {
    "1A": "F", "2A": "F", "3A": "F",  # Example seats
    "1B": "F", "2B": "F", "3B": "F",
    "X1": "X", "X2": "X",  # Aisles
    "S1": "S", "S2": "S"   # Storage areas
}

def check_availability(seat):#creating a function for checking seats availability
    if seat in seats:
        if seats[seat] == "F":
            return "Seat is available."
        else:
            return "Seat is not available."
    else:
        return "Invalid seat."

def book_seat(seat): #creating a function for booking seats
    if seat in seats and seats[seat] == "F":
        seats[seat] = "R"
        return "Seat booked successfully."
    else:
        return "Seat cannot be booked."

def book_multiple_seats(seat_list): #creating a functioon to book multiple seats at once 
    for seat in seat_list:
        if seat in seats and seats[seat] == "F":
            seats[seat] = "R"
            print(f"Seat {seat} booked successfully.")
        else:
            print(f"Seat {seat} cannot be booked.")

def free_seat(seat): #creating a function for freeing seats
    if seat in seats and seats[seat] == "R":
        seats[seat] = "F"
        return "Seat freed successfully."
    else:
        return "Seat cannot be freed."

def show_booking_status(): #creating a function for showing whats booked 
    for seat, status in seats.items():
        print(f"{seat}: {status}")

while True:  #creating a menu with the options
    print("\nMenu:")
    print("1. Check availability of seat")
    print("2. Book a seat")
    print("3. Book multiple seats")
    print("4. Free a seat")
    print("5. Show booking status")
    print("6. Exit")

    choice = input("Enter your choice: ") #getting choice

#doing whats choosen from menu using the functions
    if choice == "1":
        seat = input("Enter seat number: ")
        print(check_availability(seat))
    elif choice == "2":
        seat = input("Enter seat number: ")
        print(book_seat(seat))
    elif choice == "3":
        seat_list = input("Enter seat numbers (comma-separated, e.g., 1A,2B,3C): ").split(",")
        book_multiple_seats(seat_list)
    elif choice == "4":
        seat = input("Enter seat number: ")
        print(free_seat(seat))
    elif choice == "5":
        show_booking_status()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")
