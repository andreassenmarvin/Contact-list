class Contact:

    contact_list = []

    def __init__(self, fist_name, last_name, number, email):

        self.first_name = fist_name
        self.last_name = last_name
        self.number = number
        self.email = email


    def save_contact(self):
        Contact.contact_list.append(self)


    def delete_contact(self):
        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        Contact.contact_list.remove(self)


    @classmethod
    def find_by_number(cls, number):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for contact in cls.contact_list:
            if contact.number == number:
                return contact