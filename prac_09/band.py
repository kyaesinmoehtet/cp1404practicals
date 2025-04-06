"""
CP1404/CP5632 Practical
Band class, extends guitar class
"""
from musician import Musician

class Band(Musician):
    """Represent a Band class"""

    def __init__(self, name=""):
        """Initialise a band"""
        super().__init__(name)
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band"""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def __repr__(self):
        """Return a string representation of a Band, showing the variables."""
        return str(vars(self))

    def add(self, musician):
        """Add an musician to a Band"""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the instrument playing their first (or no) instrument for each musician"""
        musicians_and_instruments =[]
        for musician in self.musicians:
            musicians_and_instruments.append(musician.play())
        return "\n".join(musicians_and_instruments)

