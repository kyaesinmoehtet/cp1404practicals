"""
CP1404 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_details(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    with open(FILENAME, "r") as input_file:
        for line in input_file:
            line = line.strip()  # Remove the \n
            parts = line.split(',')  # Separate the data into its parts
            parts[2] = int(parts[2])  # Make the number an integer
            data.append(parts)  # Add the processed line to the data list
    return data


def display_subject_details(data):
    """Display subject details in a formatted way."""
    for subject_data in data:
        print(f"{subject_data[0]} is taught by {subject_data[1]} and has {subject_data[2]} students")


if __name__ == "__main__":
    main()