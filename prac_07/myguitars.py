"""
CP1404/CP5632 Practical
Client program for Guitar class
"""
from guitar import Guitar

def main():
    """Store guitars in list, display guitar information"""
    guitars = load_data()
    guitars.sort()
    display_guitar(guitars)

    name = str(input("Name: "))
    while name != "":
        guitar_data = get_guitar_data(name)
        print(f"{guitar_data} added.")
        guitars.append(guitar_data)
        name = str(input("Name: "))

    save_guitars(guitars)


def save_guitars(guitars):
    """Writes out guitars to csv file"""
    with open('guitars.csv', 'w') as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


def get_guitar_data(name):
    """Make new Guitar object from user input"""
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar_data = Guitar(name, year, cost)
    return guitar_data


def display_guitar(guitars):
    """Print information of guitars"""
    for guitar in guitars:
        print(guitar)


def load_data():
    """Read guitar data from csv file"""
    guitars = []
    with open('guitars.csv', 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], parts[1], float(parts[2]))
            guitars.append(guitar)
    return guitars


main()
