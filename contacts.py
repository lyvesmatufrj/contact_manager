contacts = []


def add_contact(name: str, phone: str):
    # incluir email em modificações futuras
    contact = {'name': name, 'phone': phone}
    contacts.append(contact)
    print(f"Contact {name} added sucessfully")


def remove_contact(name: str):
    global contacts
    contacts = [contact for contact in contacts if contact['name'] != name]
    print(f"Contact {name} removed sucessfully")


def list_contacts():
    if not contacts:
        print("No contacts found")
    else:
        print("\nContacts list:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
