"""
CP1404 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    num_months = int(input("How many months? "))

    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_income_report(incomes)


def print_income_report(incomes):
    """Prints the income report with cumulative totals."""
    print("\nIncome Report\n-------------")
    cumulative_total = 0
    for month, income in enumerate(incomes, start=1):
        cumulative_total += income
        print(f"Month {month:2} - Income: ${income:9.2f}         Total: ${cumulative_total:9.2f}")


if __name__ == "__main__":
    main()