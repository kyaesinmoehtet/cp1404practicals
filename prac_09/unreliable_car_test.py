"""
CP1404/CP5632 Practical
Client program to test UnreliableCar class
"""

from unreliable_car import UnreliableCar
import random

car1 = UnreliableCar("Good car", 100, 90)
car2 = UnreliableCar("Bad car", 100, 10)

for i in range(1, 16):
    random_distance = random.randint(5,15)
    print(f"Attempt {i}: Drive {random_distance} km")
    print(f"{car1.name} drove {car1.drive(random_distance)} km\n{car2.name} drove {car2.drive(random_distance)} km\n")

print(car1)
print(car2)