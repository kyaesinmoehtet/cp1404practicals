"""
CP1404/CP5632 Practical
SilverServiceTaxi class, extends Taxi class
"""
from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi class"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string like a Car but with current fare distance and flagfall"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
