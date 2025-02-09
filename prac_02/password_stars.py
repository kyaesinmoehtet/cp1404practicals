def get_password():
    password = input("Enter your password: ")
    while len(password) < 1:
        print("Password must not be empty.")
        password = input("Enter your password: ")
    return password

def print_stars(password):
    print("*" * len(password))

def main():
    password = get_password()
    print_stars(password)

if __name__ == "__main__":
    main()