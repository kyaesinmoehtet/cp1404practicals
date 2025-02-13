try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print(f"The result is {result}")
except ValueError:
    print("Numerator and denominator must be valid integers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Questions and Answers:

# 1. When will a ValueError occur?
# A ValueError occurs if the user enters a non-integer value for the numerator or denominator,
# such as letters or special characters (e.g., "abc" or "$%^").

# 2. When will a ZeroDivisionError occur?
# A ZeroDivisionError occurs when the user enters 0 as the denominator,
# because division by zero is undefined.

# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# Yes, by adding a check before performing the division to ensure the denominator is not zero.

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        result = numerator / denominator
        print(f"The result is {result}")
except ValueError:
    print("Numerator and denominator must be valid integers!")
print("Finished.")