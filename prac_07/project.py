"""
CP1404/CP5632 Practical
Project class
"""

import datetime

class Project:
    """Represent information about a project."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Construct a Project from the given values."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def is_complete(self):
        """Check if completion percentage is 100"""
        return self.completion_percentage == 100

    def __lt__(self, project2):
        """Sort project by priority in ascending order"""
        return self.priority < project2.priority

    def __str__(self):
        """Return string of Project object"""
        return f"{self.name}, start: {self.start_date.strftime("%d/%m/%Y")}, priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, completion: {self.completion_percentage}%"
