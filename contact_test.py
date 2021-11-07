import unittest
from contact import Contact

class TestContact(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''

        self.new_contact = Contact("Marvin", "Macharia", "0759082650", "marvin@gmail.com") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_contact.first_name, "Marvin")
        self.assertEqual(self.new_contact.last_name, "Macharia")
        self.assertEqual(self.new_contact.number, "0759082650")
        self.assertEqual(self.new_contact.email, "marvin@gmail.com")


    def test_save_contact(self):
        '''
        save_contact method saves contact objects into contact_list
        '''

        self.new_contact.save_contact() # saving the new contact
        self.assertEqual(len(Contact.contact_list),1)


    def save_multiple_contacts(self):
        '''
        test_save_multiple_contact to check if we can save multiple contact
        objects to our contact_list
        '''

        self.new_contact.save_contact()
        test_contact = Contact("Test", "User", "1234567890", "test@gmail.com") # new contact
        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list), 2)

if __name__ == '__main__':
    unittest.main()