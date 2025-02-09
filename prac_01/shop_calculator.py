def calculate_total(prices):
    total = sum(prices)
    if total > 100:
        total *= 0.9
    return total

def main():
    print("Shop Calculator")
    num_items = int(input("Enter the number of items: "))
    prices = []

    for i in range(num_items):
        price = float(input(f"Enter price of item {i + 1}: $"))
        prices.append(price)

    total = calculate_total(prices)
    print(f"Total cost: ${total:.2f}")

if __name__ == "__main__":
    main()