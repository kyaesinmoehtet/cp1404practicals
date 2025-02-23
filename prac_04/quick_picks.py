import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6

def generate_quick_pick():
    quick_pick = set()
    while len(quick_pick) < NUMBERS_PER_LINE:
        quick_pick.add(random.randint(MIN_NUMBER, MAX_NUMBER))
    return sorted(quick_pick)

def main():
    num_quick_picks = int(input("How many quick picks? "))
    if num_quick_picks <= 0:
        print("Please enter a positive number.")
        return

    for _ in range(num_quick_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{num:2}" for num in quick_pick))

if __name__ == "__main__":
    main()