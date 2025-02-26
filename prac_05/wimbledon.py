import csv

def main():
    filename = "wimbledon.csv"
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip header
        champion_wins = {}
        countries = set()
        for row in reader:
            champion = row[2]
            country = row[1]
            if champion in champion_wins:
                champion_wins[champion] += 1
            else:
                champion_wins[champion] = 1
            countries.add(country)

    print("Wimbledon Champions:")
    for champion, wins in sorted(champion_wins.items()):
        print(f"{champion} {wins}")

    print("\nThese countries have won Wimbledon:")
    print(", ".join(sorted(countries)))

if __name__ == "__main__":
    main()