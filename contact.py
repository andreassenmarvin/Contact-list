class Contact:

    contact_list = []

    def __init__(self, fist_name, last_name, number, email):

        self.first_name = fist_name
        self.last_name = last_name
        self.number = number
        self.email = email

    def save_contact(self):
        Contact.contact_list.append(self)
        