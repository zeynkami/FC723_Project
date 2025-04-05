import sqlite3 #Importing SQLite library for database operations
import random #Importing random module to generate random values
import string #Importing string module to work with string constants

class DatabaseManager: #Class to manage database operations for bookings
    def __init__(self, db_name='bookings.db'): #Initializing the database connection and create the bookings table
        self.conn = sqlite3.connect(db_name) #Connecting to the specified SQLite database
        self.cursor = self.conn.cursor() #Creating a cursor for the SQL commands
        self.create_table() #to create the bookings table if it doesn't exist

    def create_table(self): #creating a function for showing whats booked 
        self.cursor.execute(  #to create the bookings table
            "CREATE TABLE IF NOT EXISTS bookings ("
            "reference TEXT PRIMARY KEY,"
            "passport TEXT,"
            "first_name TEXT,"
            "last_name TEXT,"
            "seat TEXT)"
        )
        self.conn.commit()

    def insert_booking(self, reference, passport, first_name, last_name, seat):
        self.cursor.execute(  #to insert a new booking record into the database
            "INSERT INTO bookings (reference, passport, first_name, last_name, seat) "
            "VALUES (?, ?, ?, ?, ?)",
            (reference, passport, first_name, last_name, seat)
        )
        self.conn.commit()

    def delete_booking(self, reference):
        self.cursor.execute( #to delete a booking from the database using reference ID
            "DELETE FROM bookings WHERE reference = ?",
            (reference,)
        )
        self.conn.commit()


class SeatManager: #Initializing the database connection and create the bookings table
    def __init__(self):
        self.seats = {
            "1A": "F", "2A": "F", "3A": "F",
            "1B": "F", "2B": "F", "3B": "F",
            "X1": "X", "X2": "X",
            "S1": "S", "S2": "S"
        }

    def check_availability(self, seat): #creating a function for checking seats availability
        if seat in self.seats:
            return "Seat is available." if self.seats[seat] == "F" else "Seat is not available."
        return "Invalid seat."

    def mark_seat_booked(self, seat, reference):#creating a function for booking seats
        self.seats[seat] = reference

    def mark_seat_free(self, seat):
        self.seats[seat] = "F"

    def get_seat_reference(self, seat):
        return self.seats[seat]

    def is_seat_free(self, seat):
        return self.seats.get(seat) == "F"

    def is_seat_valid(self, seat):
        return seat in self.seats

    def show_status(self):
        for seat, status in self.seats.items():
            print(f"{seat}: {status}")


class ReferenceGenerator:
    def generate():
        characters = string.ascii_letters + string.digits #Combining letters and digits
        return ''.join(random.choice(characters) for _ in range(8)) #Generating 8 random characters


class BookingSystem: #Initializing the database connection and create the bookings table
    def __init__(self):
        self.db = DatabaseManager()
        self.seat_manager = SeatManager()

    def book_seat(self, seat, passport, first_name, last_name):#creating a function for booking seat
        if self.seat_manager.is_seat_valid(seat) and self.seat_manager.is_seat_free(seat):
            reference = ReferenceGenerator.generate() #Generating a booking reference
            self.seat_manager.mark_seat_booked(seat, reference)
            self.db.insert_booking(reference, passport, first_name, last_name, seat)  #Inserting booking details into the database
            return f"Seat booked successfully. Reference: {reference}"
        return "Seat cannot be booked."

    def book_multiple_seats(self, seat_list, passport, first_name, last_name):#creating a function to book multiple seats at once 
        for seat in seat_list:
            print(self.book_seat(seat.strip(), passport, first_name, last_name))

    def free_seat(self, seat):#creating a function for freeing seats
        if self.seat_manager.is_seat_valid(seat) and not self.seat_manager.is_seat_free(seat):
            reference = self.seat_manager.get_seat_reference(seat)
            self.seat_manager.mark_seat_free(seat)
            self.db.delete_booking(reference)
            return "Seat freed successfully."
        return "Seat cannot be freed."

    def check_availability(self, seat):
        return self.seat_manager.check_availability(seat)

    def show_booking_status(self):
        self.seat_manager.show_status()

    def menu(self): #creating a menu with the options
        while True:
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
                print(self.check_availability(seat))
            elif choice == "2":
                seat = input("Enter seat number: ")
                passport = input("Enter passport number: ")
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                print(self.book_seat(seat, passport, first_name, last_name))
            elif choice == "3":
                seat_list = input("Enter seat numbers (comma-separated, e.g., 1A,2B,3B): ").split(",")
                passport = input("Enter passport number: ")
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                self.book_multiple_seats(seat_list, passport, first_name, last_name)
            elif choice == "4":
                seat = input("Enter seat number: ")
                print(self.free_seat(seat))
            elif choice == "5":
                self.show_booking_status()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    system = BookingSystem()
    system.menu()
