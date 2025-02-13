is_valid_input = False
while not is_valid_input:
    try:
        number = int(input("Enter a valid integer: "))
        is_valid_input = True  # If input is valid, exit the loop
    except ValueError:
        print("Invalid input; please enter a valid integer.")

print(f"You entered {number}")
