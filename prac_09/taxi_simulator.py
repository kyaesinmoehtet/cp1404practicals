"""
CP1404/CP5632 Practical
Taxi simulator program with Taxi and SilverServiceTaxi classes
"""
from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    """Taxi simulator program"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill_to_date = 0
    print(f"Let's drive!\n{MENU}")
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            print_taxis(taxis)

            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")

        elif choice == "d":
            if current_taxi is None:
                print(f"You need to choose a taxi before you can drive")
            else:
                distance_to_drive = int(input("Drive how far? "))
                trip_fare = drive_taxi(current_taxi, distance_to_drive)
                print(f"Your {current_taxi.name} trip cost you ${trip_fare:.2f}")
                bill_to_date += trip_fare
        else:
            print("Invalid option")

        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    print_taxis(taxis)


def drive_taxi(current_taxi, distance_to_drive):
    """Drive taxi and get trip fare"""
    current_taxi.start_fare()
    current_taxi.drive(distance_to_drive)
    trip_fare = current_taxi.get_fare()
    return trip_fare


def print_taxis(taxis):
    """Display list of taxis"""
    for i in range(len(taxis)):
        print(f"{i} - {taxis[i]}")

main()


