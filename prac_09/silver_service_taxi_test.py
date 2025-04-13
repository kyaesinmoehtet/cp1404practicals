"""
CP1404/CP5632 Practical
Client program to test SilverServiceTaxi class
"""
from silver_service_taxi import SilverServiceTaxi

taxi = SilverServiceTaxi("Silver taxi", 100, 2)
taxi.drive(18)
print(taxi)
print(f"Total fare: ${taxi.get_fare():.2f}")