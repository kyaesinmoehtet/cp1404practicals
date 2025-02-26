import csv

def main():
    filename = "wimbledon.csv"
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip header
        champion_wins = {}
        countries = set()