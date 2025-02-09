def main():
    print("1. Show odd numbers between 1 and 20")
    print("2. Count in tens from 0 to 100")
    print("3. Display numbers in reverse from 20 to 1")
    print("4. Print stars based on user input")

    choice = int(input("Choose an option: "))

    if choice == 1:
        for i in range(1, 21, 2):
            print(i, end=" ")
    elif choice == 2:
        for i in range(0, 101, 10):
            print(i, end=" ")
    elif choice == 3:
        for i in range(20, 0, -1):
            print(i, end=" ")
    elif choice == 4:
        n = int(input("How many stars? "))
        print("*" * n)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()