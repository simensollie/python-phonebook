import sys

# Nested dictionary (phone book) with example entries
phonebook = {0: {'First name': 'Matt', 'Last name': 'Damon', 'Phone': '95487621', 'Address': 'Celeb Street 34'},
             1: {'First name': 'Ben', 'Last name': 'Affleck', 'Phone': '47516448', 'Address': 'Celeb Street 56'},
             2: {'First name': 'Jimmy', 'Last name': 'Kimmel', 'Phone': '41785435', 'Address': 'Celeb Street 49'},
             3: {'First name': 'Sarah', 'Last name': 'Silverman', 'Phone': '41785435', 'Address': 'Celeb Street 13'}}

# List the people in your phone book
def list_phonebook(d):
    for pid in d:
        print('\nPID:', pid + 1)
        for p_info in d[pid]:
            print(p_info + ':', d[pid][p_info])

# Add a new record to the phone book that avoids to add duplicates.
def add_record(d):
    print("Enter the information of the person you'd like to add")
    firstname = input('First name: ')
    lastname = input('Last name: ')
    phone = input('Phone: ')
    address = input('Address: ')

    duplicate = False

    for pid in d:
        if firstname == d[pid].get('First name') and lastname == d[pid].get('Last name'):
            duplicate = True

    if duplicate == True:
        print('\n# The contact is already in the phone book')
    else:
        d[len(d)] = {'First name': firstname, 'Last name': lastname, 'Phone': phone, 'Address': address}
        print('\n# The contact has been added to the phone book')

    return d

# Delete a record from the phone book using the combination First name and Last name.
def delete_record(d):
    print("Enter the name of the person you'd like to remove")
    firstname = input('First name: ')
    lastname = input('Last name: ')

    for pid in d:
        if firstname == d[pid].get('First name') and lastname == d[pid].get('Last name'):
            del d[pid]
            print('\n# The contact has been deleted')
            return d
    print('\n# The contact is not in the phone book')

# Check if a person is already in your phone book using the combination First name and Last name.
def check_record(d):
    print("Enter the name of the person you'd like to check")
    firstname = input('First name: ')
    lastname = input('Last name: ')

    for pid in d:
        if firstname == d[pid].get('First name') and lastname == d[pid].get('Last name'):
            print('\n# The contact is already in the phone book')
            return d
    print('\n# The contact is not in the phone book')

# Change a specific entry of a record.
def change_entry_in_record(d):
    print("Enter the name of the person for which you'd like to change information")
    firstname = input('First name: ')
    lastname = input('Last name: ')

    for pid in d:
        if firstname == d[pid].get('First name') and lastname == d[pid].get('Last name'):
            print("We have located your friend. Please enter which entry you'd like to change.\n"
                  "1: First name\n"
                  "2: Last name\n"
                  "3: Phone number\n"
                  "4: Address")
            entry = input("Enter a number between 1-4: ") # BUG 2 - 404 Doesnt register which selection I've made

            if entry == 1:
                d[pid]['First name'] = input('Enter a new first name: ')
                print('\n# First name has been changed')
            elif entry == 2:
                d[pid]['Last name'] = input('Enter a new last name: ')
                print('\n# Last name has been changed')
            elif entry == 3:
                d[pid]['Phone'] = input('Enter a new phone number: ')
                print('\n# Phone number has been changed')
            elif entry == 4:
                d[pid]['Adress'] = input('Enter a new address: ')
                print('\n# Address has been changed')
            else:
                print('\n# 404 - Page cannot be found')

            return d
    print('# The contact is not in the phone book')

# List the people in your phone book ordered by First name.
def ordered_list_by_first_name(d):
    ordered_d = dict(sorted(d.items(), key=lambda pid: pid[1]['First name']))

    print("Phone book ordered by first name: ")
    for pid, info in ordered_d.items():
        print('\nPerson number: ', pid)
        for key in info:
            print(key + ':', info[key])

# List the people in your phone book ordered by Last name.
def ordered_list_by_last_name(d):
    ordered_d = dict(sorted(d.items(), key=lambda pid: pid[1]['Last name']))

    print("Phone book ordered by last name: ")
    for pid, info in ordered_d.items():
        print('\nPerson number: ', pid)
        for key in info:
            print(key + ':', info[key])

# Check if there are records having the same phone number and list them.
def check_for_duplicate_phone_numbers(d):
    print('# This function is under maintenance. Please try again later.')
    return d

# Main function where we create menu and receive input
def mainmenu():
    while True:
        selection = input("""
        
----MAIN MENU----
1: List phonebook
2: Add a new record
3: Delete a record
4: Check if a person is already in your phone book
5: Change a specific entry of a record
6: List the people in your phone book ordered by first name
7: List the people in your phone book ordered by last name
8: List records with duplicate phone numbers
9: Explode into oblivion

Please enter your choice: """)

        if selection == '1':
            list_phonebook(phonebook)
        elif selection == '2':
            add_record(phonebook)
        elif selection == '3':
            delete_record(phonebook)
        elif selection == '4':
            check_record(phonebook)
        elif selection == '5':
            change_entry_in_record(phonebook)
        elif selection == '6':
            ordered_list_by_first_name(phonebook)
        elif selection == '7':
            ordered_list_by_last_name(phonebook)
        elif selection == '8':
            check_for_duplicate_phone_numbers(phonebook)
        elif selection == '9':
            print('# BOOM!')
            return False
        else:
            print('\n# 404 - Page cannot be found')

mainmenu()