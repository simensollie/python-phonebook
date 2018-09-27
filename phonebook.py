import sys

# Creating a phone book with example entries
phonebook = {0: {'First name': 'Sander', 'Last name': 'Sollie', 'Phone': '98078029', 'Address': 'Agnes Mowinckels gate 6'},
             1: {'First name': 'Simen', 'Last name': 'Sollie', 'Phone': '97616675', 'Address': 'Buggelandsbakken 56'},
             2: {'First name': 'Mathilde', 'Last name': 'Sollie', 'Phone': '98765432', 'Address': 'Kornveien 4'}}

# Function for listing the records in phone book
def list_phonebook():
    for pid in phonebook:
        print('\npid:', pid + 1)
        for p_info in phonebook[pid]:
            print(p_info + ':', phonebook[pid][p_info])

# Function for adding a record to the phonebook and checking for duplicates
def add_record():
    print("Enter the information of the person you'd like to add")
    firstname = input('First name: ')
    lastname = input('Last name: ')
    phone = input('Phone: ')
    address = input('Address: ')

    #for pid in phonebook:
    #    print(phonebook[pid].get('Phone'))

    for pid in phonebook:
        if phone in phonebook[pid]['Phone']:
            print('The contact is already in the phone book')
            break
        elif phone not in phonebook[pid]['Phone']:
            p_len = len(phonebook)
            phonebook[p_len] = {}
            phonebook[p_len]['First name'] = firstname
            phonebook[p_len]['Last name'] = lastname
            phonebook[p_len]['Phone'] = phone
            phonebook[p_len]['Address'] = address
            print('The contact has been added to the phone book')
        return True


'''
    for pid in phonebook:
        if phone is phonebook[pid].get('Phone'):
            print('The contact is already in the phone book')
            break
        else:
            phonebook_length = len(phonebook)
            phonebook[phonebook_length] = {}
            phonebook[phonebook_length]['First name'] = firstname
            phonebook[phonebook_length]['Last name'] = lastname
            phonebook[phonebook_length]['Phone'] = phone
            phonebook[phonebook_length]['Address'] = address
            print('The contact has been added to the phone book')
        return True
'''
# Deletes a contact from phone book based on first and last name
def delete_record():
    print("Enter the name of the person you'd like to remove")
    firstname = input('First name: ')
    lastname = input('Last name: ')


# Main function where we create menu and receive input
def mainmenu():
    while True:
        selection = input("""
        
----MAIN MENU----
1: List phonebook
2: Add a new record
3: Delete a record
4: Check if a person is in the phonebook
5: Quit/Log Out

Please enter your choice: """)

        if selection == '1':
            list_phonebook()
        elif selection == '2':
            add_record()
        elif selection == '3':
            delete_record()
        elif selection == '4':
            print('Checking')
        elif selection == '5':
            return False
        else:
            return True

mainmenu()