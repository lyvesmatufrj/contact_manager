from contacts import add_contact, remove_contact, list_contacts
from utils import validate_phone


def main():
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. List Contacts")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            if validate_phone(phone):
                add_contact(name, phone)
            else:
                print("Invalid phone number. It should be 10 digits.")
        elif choice == '2':
            name = input("Enter the name of the contact to remove: ")
            remove_contact(name)
        elif choice == '3':
            list_contacts()
        elif choice == '4':
            print("Exiting Contact Manager.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
