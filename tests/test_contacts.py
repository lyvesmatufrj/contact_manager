import unittest
from contact_manager.contacts import (Contact,
                                      PersonalContact,
                                      BusinessContact,
                                      ContactGroup)


class TestContactGroup(unittest.TestCase):
    def setUp(self):
        self.family_group = ContactGroup("Family")
        self.work_group = ContactGroup("Work")

        self.contact1 = PersonalContact(name="Alice",
                                        phone="123456789",
                                        email="alice@example.com",
                                        birthday="1990-01-01")
        self.contact2 = BusinessContact(name="Bob",
                                        phone="987654321",
                                        email="bob@abc.com",
                                        company="ABC Inc.",
                                        job_title="Software Engineer")

    def test_add_contact(self):
        self.family_group.add_contact(self.contact1)
        self.assertIn(self.contact1, self.family_group.contacts)

    def test_remove_contact(self):
        self.family_group.add_contact(self.contact1)
        self.family_group.remove_contact(self.contact1.name)
        self.assertNotIn(self.contact1, self.family_group.contacts)

    def test_list_contacts(self):
        self.family_group.add_contact(self.contact1)
        self.family_group.add_contact(self.contact2)
        self.family_group.list_contacts()


if __name__ == "__main__":
    unittest.main()
