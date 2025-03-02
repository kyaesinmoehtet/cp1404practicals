"""
CP1404 Practical
State names in a dictionary
File needs reformatting
"""

# Reformat dictionary to follow PEP 8
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

# Print the dictionary
print(CODE_TO_NAME)

# Function to print all states neatly
def print_states():
    for code, name in CODE_TO_NAME.items():
        print(f"{code:<3} is {name}")

# Main program
def main():
    print_states()
    state_code = input("Enter short state: ").upper()
    while state_code != "":
        try:
            print(state_code, "is", CODE_TO_NAME[state_code])
        except KeyError:
            print("Invalid short state")
        state_code = input("Enter short state: ").upper()

main()