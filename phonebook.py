import sys

# Creating a phonebook
phonebook = {0: {'firstname': 'Sander', 'surname': 'Sollie', 'phonenumber': '98078029', 'address': 'Agnes Mowinckels gate 6'}, 
			1: {'firstname': 'Simen', 'surname': 'Sollie', 'phonenumber': '97616675', 'address': 'Buggelandsbakken 56'}, 
			2: {'firstname': 'Mathilde', 'surname': 'Sollie', 'phonenumber': '98765432', 'address': 'Kornveien 4'}}

# Function for adding a record to the phonebook and checking for duplicates
def addRecord():
    firstname = input('First name: ')
    surname = input('Last name: ')
    phonenumber = input('Phone number: ')
    address = input('Address: ')

    for pid in phonebook:
        print(phonebook[pid].get('phonenumber'))

    for pid in phonebook:
        if phonenumber == phonebook[pid].get('phonenumber'):
            print('The contact is already in the phonebook')
            break
        else:
            phonebook_length = len(phonebook)
            phonebook[phonebook_length] = {}
            phonebook[phonebook_length]['firstname'] = firstname
            phonebook[phonebook_length]['surname'] = surname
            phonebook[phonebook_length]['phonenumber'] = phonenumber
            phonebook[phonebook_length]['address'] = address
            print('The contact has been added to the phonebook')
        return True

def deleteRecord(name):
    deletedList = phonebook.popitem()
    print(phonebook)

def noDuplicate(name):
    if phonebook.get(name):
        print('The contact is already in the phonebook')
    else:
        phonebook[name] = True
        print('The contact can be added to the phonebook')

menu = {}
menu['1'] = 'Add a new record'
menu['2'] = 'Delete a record'
menu['3'] = 'Check if a person is in the phonebook'
menu['4'] = 'Quit/exit'

# Main function where we create menu and choose action
def mainmenu():
    while True:
        options = list(menu.keys())
        options.sort()

        for entry in options:
            selection = input("""
            
   ----MAIN MENU----
1: List phonebook
2: Add a new record
3: Delete a record
4: Check if a person is in the phonebook
5: Quit/Log Out

Please enter your choice: """)

            if selection == '1':
                for pid in phonebook:
                    print('\npid:', pid+1)
                    for person_info in phonebook[pid]:
                        print(person_info + ':', phonebook[pid][person_info])
            elif selection == '2':
                addRecord()
            elif selection == '3':
                deleteRecord()
            elif selection == '4':
                print('Checking')
            elif selection == '5':
                return False
            else:
                return True

mainmenu()