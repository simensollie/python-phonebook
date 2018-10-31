class Contact(object):
    def __init__(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone

    def __str__(self):
        s = '\nname: ' + self.name + ' ' + self.surname
        s += '\nphone: ' + self.phone
        return s


class BusinessContact(Contact):
    def __init__(self, name, surname, phone, company, businessAdress):
        Contact.__init__(self, name, surname, phone)
        self.company = company
        self.businessAddress = businessAdress


class PersonalContact(Contact):
    def __init__(self, name, surname, phone, homeAddress, relationship):
        Contact.__init__(self, name, surname, phone)
        self.homeAddress = homeAddress
        self.relationship = relationship


class PhoneBook(object):
    def __init__(self):
        self.contacts = {}

    def __add__(self, name, surname, phone):
        c = Contact(name, surname, phone)
        self.contacts[name + ' ' + surname] = c

    def __call__(self, name):
        return self.contacts[name]

    def __str__(self):
        s = ''
        for p in sorted(self.contacts):
            s += '\n' + str(self.contacts[p])
        return s

    def addContact(self):
        print("\nEnter the information of the contact you'd like to add")
        name = input('First name: ')
        surname = input('Last name: ')
        phone = input('Phone: ')
        selection = input("""
1: Business
2: Personal
Other: Neither

Personal or Business? Enter: """)

        if selection == '1':
            company = input('\nCompany: ')
            businessAddress = input('Address: ')
            c = BusinessContact(name, surname, phone, company, businessAddress)
        elif selection == '2':
            homeAddress = input('\nAddress: ')
            relationship = input('Raltionship: ')
            c = PersonalContact(name, surname, phone, homeAddress, relationship)
        else:
            c = Contact(name, surname, phone)

        self.contacts[name + ' ' + surname] = c
        print("\n# Contact added")

    def delete(self):
        print("\nEnter the name of the contact you'd like to delete")
        name = input('First name: ')
        surname = input('Last name: ')

        del self.contacts[name + ' ' + surname]
        print("\n# Contact deleted")

    def listByType(self):
        s = ''
        for p in sorted(self.contacts):
            s += '\n' + str(self.contacts[p])
        return s


def main():
    p = PhoneBook()
    p.__add__('Johnny', 'Depp', '32165487')
    p.__add__('Orlando', 'Bloom', '98765432')
    p.__add__('Keira', 'Knightly', '12345678')

    while True:
        selection = input("""

    ----MAIN MENU----
    1: Add contact
    2: Search
    3: Delete
    4: List phone book by type
    5: Explode into oblivion

    Please enter your choice: """)

        if selection == '1':
            p.addContact()
        elif selection == '2':
            print('\n# 404 - Page cannot be found')
        elif selection == '3':
            p.delete()
        elif selection == '4':
            p.listByType()  # NOT WORKING
            print(p)        # defined by method -> def __str__(self):
        elif selection == '5':
            print('# BOOM!')
            return False
        else:
            print('\n# 404 - Page cannot be found')


main()
