"""
CP1404/CP5632 Practical
UnreliableCar class, extends Car class
"""
from car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car that includes randomness"""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car."""
        return f"{super().__str__()}"

    def drive(self, distance):
        """Drive like parent Car depending on reliability."""
        if random.randint(0, 100) >= self.reliability:
            distance = 0
        return super().drive(distance)

