"""
Emails
Estimate: 55 minutes
Actual: 40 minutes
"""

def main():
    emails_to_names = {}
    while True:
        email = input("Email: ").strip()
        if not email:
            break
        name = extract_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation != "" and confirmation != "y":
            name = input("Name: ").strip().title()
        emails_to_names[email] = name
    print_emails_and_names(emails_to_names)

def extract_name_from_email(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(part.title() for part in parts)
    return name

def print_emails_and_names(emails_to_names):
    for email, name in emails_to_names.items():
        print(f"{name} ({email})")

main()