import random

# Constants
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
FILENAME = "output.txt"  # Output file name

# Initial setup
price = INITIAL_PRICE
number_of_days = 0

# Open file for writing
out_file = open(FILENAME, 'w')

# Display the starting price
print(f"Starting price: ${price:,.2f}")
print(f"Starting price: ${price:,.2f}", file=out_file)

# Simulation loop
while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    number_of_days += 1

    # Determine if price goes up or down
    if random.randint(1, 2) == 1:
        # Increase by 0 to MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # Decrease by 0 to MAX_DECREASE
        price_change = random.uniform(-MAX_DECREASE, 0)

    # Calculate new price and ensure it's rounded to 2 decimal places
    price *= (1 + price_change)
    price = round(price, 2)

    # Display and write the current day's price
    print(f"On day {number_of_days} price is: ${price:,.2f}")
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

# Close the file at the end
out_file.close()
