"""CP1404/CP5632 Practical - Car class example."""


class Car:
    """Represent a Car object."""

    def __init__(self, fuel=0, name=""):

        self.fuel = fuel
        self._odometer = 0
        self.name = name

    def __str__(self):
        """Return a string representation of the car."""
        return f"Car={self.name}, fuel={self.fuel}, odometer={self._odometer}"

    def add_fuel(self, amount):

        self.fuel += amount

    def drive(self, distance):

        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance
