"""
Wimbledon Champions Data Processor

Estimate time: 30 minutes
Actual time: 45 minutes
"""


def read_wimbledon_data(filename):
    """Read and process the Wimbledon CSV file."""
    wimbledon_data = []
    with open(filename, "r", encoding="utf-8-sig") as file:
        next(file)  # Skip header row
        for line in file:
            parts = line.strip().split(',')
            year, champion, country = parts[0], parts[1], parts[2]
            wimbledon_data.append([year, champion, country])
    return wimbledon_data


def process_champions(wimbledon_data):
    """Process the champions and their number of wins."""
    champions_dict = {}
    for entry in wimbledon_data:
        champion = entry[1]
        champions_dict[champion] = champions_dict.get(champion, 0) + 1
    return champions_dict


def process_countries(wimbledon_data):
    """Get a set of unique champion countries."""
    countries = set(entry[2] for entry in wimbledon_data)
    return sorted(countries)


def main():
    """Main function to coordinate reading, processing, and displaying data."""
    filename = "wimbledon.csv"
    wimbledon_data = read_wimbledon_data(filename)
    champions_dict = process_champions(wimbledon_data)
    countries_list = process_countries(wimbledon_data)

    print("Wimbledon Champions:")
    for champion, wins in champions_dict.items():
        print(f"{champion} {wins}")

    print(f"\nThese {len(countries_list)} countries have won Wimbledon:")
    print(", ".join(countries_list))

main()