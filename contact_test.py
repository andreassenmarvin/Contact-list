import unittest
from contact import Contact

class TestContact(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''

        self.new_contact = Contact("Marvin", "Macharia", "0759082650", "marvin@gmail.com") # create contact object


    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''

        Contact.contact_list = []


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


    def test_save_multiple_contacts(self):
        '''
        test_save_multiple_contact to check if we can save multiple contact
        objects to our contact_list
        '''

        self.new_contact.save_contact()
        test_contact = Contact("Test", "User", "1234567890", "test@gmail.com") # new contact
        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list),2)


    def test_delete_contact(self):
        '''
        test_delete_contact to test if we can remove a contact from our contact list
        '''

        self.new_contact.save_contact()
        test_contact = Contact("Test", "User", "1234567890", "test@gmail.com") # new contact
        test_contact.save_contact()

        self.new_contact.delete_contact() # Deleting a contact object
        self.assertEqual(len(Contact.contact_list),1)
        

    def test_find_contact_by_number(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''
        
        self.new_contact.save_contact()
        test_contact = Contact("Test", "User", "0987654321", "test@gmail.com") # new contact
        test_contact.save_contact()

        found_contact = Contact.find_by_number("0987654321")
        self.assertEqual(found_contact.number,test_contact.number)



if __name__ == '__main__':
    unittest.main()