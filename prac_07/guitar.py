"""
CP1404/CP5632 Practical
Guitar class
"""
CURRENT_YEAR = 2025
VINTAGE_AGE = 50
class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """Calculate age based on current year"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Check if guitar age is greater or equal to vintage age"""
        return self.get_age() >= VINTAGE_AGE


    def __str__(self):
        """Return string of Guitar object"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, guitar2):
        """Sort guitars by year in ascending order"""
        return self.year < guitar2.year
