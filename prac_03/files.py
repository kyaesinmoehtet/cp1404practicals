# Part 1: Write name to file
name = input("What is your name? ")

# Open file in write mode and write name
out_file = open('name.txt', 'w')
out_file.write(name)
out_file.close()

# Part 2: Read name from file and print greeting
in_file = open('name.txt', 'r')
name = in_file.read().strip()  # Strip any extra whitespace or newline
in_file.close()

print(f"Hi {name}!")

# Part 3: Add first two numbers
with open('numbers.txt', 'r') as file:
    first_number = int(file.readline().strip())  # Read first line and convert to int
    second_number = int(file.readline().strip())  # Read second line and convert to int

    result = first_number + second_number
    print(f"The sum of the first two numbers is: {result}")

# Part 4: Sum all numbers in file
total = 0

with open('numbers.txt', 'r') as file:
    for line in file:
        total += int(line.strip())  # Convert each line to int and add to total

print(f"The total of all numbers is: {total}")






