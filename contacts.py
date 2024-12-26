class Contact:
    def __init__(self, name: str, phone: str, email: str):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"


class PersonalContact(Contact):
    def __init__(self, name: str, phone: str, email: str, birthday: str):
        super().__init__(name, phone, email)
        self.birthday = birthday

    def __str__(self):
        return f"{super().__str__()}, Birthday {self.birthday}"


class BusinessContact(Contact):
    def __init__(self, name: str, phone: str, email: str, company: str, job_title: str):
        super().__init__(name, phone, email)
        self.company = company
        self.job_title = job_title

    def __str__(self):
        return f"{super().__str__()}, Company: {self.company}, Job Title: {self.job_title}"


class ContactGroup:
    def __init__(self, group_name: str):
        self.group_name = group_name
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact {contact.name} added to group {self.group_name}.")

    def remove_contact(self, contact_name):
        self.contacts = [contact for contact in self.contacts if contact.name != contact_name]

    def list_contacts(self):
        if not self.contacts:
            print(f"No contacts in group {self.group_name}")
        else:
            print(f"Contacts in group {self.group_name}:")
            for contact in self.contacts:
                print(contact)
