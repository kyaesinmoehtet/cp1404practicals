def determine_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def main():
    score = float(input("Enter initial score: "))
    while True:
        print("(G)et score\n(P)rint result\n(Q)uit")
        choice = input(">>> ").upper()
        if choice == "G":
            score = float(input("Enter new score: "))
        elif choice == "P":
            print(determine_grade(score))
        elif choice == "Q":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()