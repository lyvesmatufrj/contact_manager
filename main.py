from contacts import PersonalContact, BusinessContact, ContactGroup


def main():
    family_group = ContactGroup("Family")
    work_group = ContactGroup("Work")

    contact1 = PersonalContact(name="John Doe", phone="555-1234", email="john@example.com",
                               birthday="2000-01-01")
    contact2 = BusinessContact(name="Jane Doe", phone="555-5678", email="jane@company.com",
                               company="TechCorp", job_title="Engineer")

    family_group.add_contact(contact1)
    work_group.add_contact(contact2)

    family_group.list_contacts()
    work_group.list_contacts()

    family_group.remove_contact("John Doe")
    family_group.list_contacts()


if __name__ == "__main__":
    main()
