import sys
from collections import OrderedDict
from collections import Counter

#This is the dictionary for the phonebook. It consist of 5 contacts
#that has been added in a nested dictionary
phonebook = {1: {'firstname': 'Aksel', 'surname': 'Henning', 'phonenumber': '98078029', 'address': 'Bergensveien 2'},
2: {'firstname': 'Tone', 'surname': 'Damli', 'phonenumber': '96084185', 'address': 'Buggelandsbakken 107'},
3: {'firstname': 'Magnus', 'surname': 'Holt', 'phonenumber': '90178513', 'address': 'Kong Oscars gate 13'},
4: {'firstname': 'Helene', 'surname': 'Ulsvik', 'phonenumber': '92375971', 'address': 'Helleveien 42'},
5: {'firstname': 'Kari', 'surname': 'Sigde', 'phonenumber': '45856031', 'address': 'Breiviksbakken 1'},
6: {'firstname': 'Per', 'surname': 'Askeladden', 'phonenumber': '98078029', 'address': 'Bergensveien 2'}}

def addRecord():
    firstname = input('What is your first name? ')
    surname = input('What is your surname? ')
    phonenumber = input('What is your phonenumber? ')
    address = input('What is your address? ')

    for x in phonebook:
        if firstname == phonebook[x].get('firstname') and surname == phonebook[x].get('surname'):
            print('The contact is already in the phonebook')
            break
        else:
            print('The contact has been added to the phonebook')
            phonebook[len(phonebook) + 1] = {'firstname': firstname, 'surname': surname, 'phonenumber': phonenumber, 'address': address}

        return



def deleteRecord(d):
    deleteFirstname = input('What is the first name of the contact you want to delete? ')
    deleteSurname = input('What is the surname of the contact you want to delete? ')

    for x in d:
        if deleteFirstname == d[x].get('firstname') and deleteSurname == d[x].get('surname'):
            del d[x]
            print('The contact has been deleted')
            return d
    print('The contact is not in the phonebook')

def duplicate(d):
    dupl_firstname = input('What is the contact\'s first name? ')
    dupl_surname = input('What is the contact\'s surname? ')

    for x in d:
        if dupl_firstname == d[x].get('firstname') and dupl_surname == d[x].get('surname'):
            print('The contact is already in the phonebook')
            return d
    print('The contact is not in the phonebook')

def changeRecord(d):

    changeFirstname = input('What is the contact\'s first name? ')
    changeSurname = input('What is the contact\'s surname? ')
    print(' ')

    for x in d:
        if changeFirstname == d[x].get('firstname') and changeSurname == d[x].get('surname'):
            print('Please put in the contact\'s new information: ')
            d[x]['firstname'] = input('What is the persons first name? ')
            d[x]['surname'] = input('What is the persons surname? ')
            d[x]['phonenumber'] = input('What is the persons phonenumber? ')
            d[x]['address'] = input('What is the persons address? ')
            return d
    print('The contact is not in the phonebook')

# make a function to list the phonebook after the contacts first name
def listFirstname():

    print(sorted(phonebook, key=lambda x: (phonebook[x]['firstname'])))

    sortedphonebook = OrderedDict(sorted(phonebook.items(), key=lambda x: (phonebook[1]['firstname'])))
    print(sortedphonebook)


def listSurname():
    sortedSurname = phonebook.items()
    print(sortedSurname)

    for pNumber, pInfo in phonebook.items():
        print('\nPerson number:', 0)
        for key in pInfo:
            print(key + ':', pInfo[key])

        for pNumber, pInfo in phonebook.items():
            print("\nPerson number:", pNumber)
            for key in pInfo:
                print(key + ':', pInfo[key])



def samePhonenumber(d):

    '''
    encountered_entries = set()
    for key, entry in d.items():
        if (entry['phonenumber']) in encountered_entries:
            print(d[key])
        else:
            encountered_entries.add((entry['phonenumber']))
    '''

    c = Counter(x for xs in d.values() for x in xs)
    print(c)

    d_dups = {k: [v for v in vs if c[v] > 1] for k, vs in d.items()}

    print(d_dups)

# a main menu to choose between the different functions in the program.
# make a dictionary to put the different options in
menu = {0: ''}

# make a function for the mainmenu.
def mainmenu():
# the loop will go as long as the expression evaluates as True
    while True:
        options = list(menu.keys())
# make a new list (options) that contains the keys in the menu dictionary
# make a for loop where the user is asked which option he/she wants
        for choosing in options:
            selection = input("""

                                  ----MENU----
                              1: List the phonebook
                              2: Add a new record
                              3: Delete a record
                              4: Check if a contact is in the phonebook
                              5: Change an excisting record
                              6: Sort the phonebook by First name
                              7: Sort the phonebook by surname
                              8: Check if two records have the same phonenumber
                              9: Quit/Log Out

                              Please enter your choice: """)
            print(' ')

# if the user write 1, a list of the phonebook comes up
# if the user write 2, you can add a new record and so on
# to exit the program the user have to write 7 where the loop no longer
# expresses True, but False and the program Buggelandsbakken
# if the user type something other than the choices available it presidents
# 'please choose a valid number and a new number has to be picked'
            if selection == '1':
                for pNumber, pInfo in phonebook.items():
                    print("\nPerson number:", pNumber)
                    for key in pInfo:
                        print(key + ':', pInfo[key])
            elif selection == '2':
                addRecord()
            elif selection == '3':
                deleteRecord(phonebook)
            elif selection == '4':
                duplicate(phonebook)
            elif selection == '5':
                changeRecord(phonebook)
            elif selection == '6':
                listFirstname()
            elif selection == '7':
                listSurname()
            elif selection == '8':
                samePhonenumber(phonebook)
            elif selection == '9':
                return False
            else:
                print('Please choose a valid number')
                # end of mainmenu function

mainmenu() # this is what starts the mainmenu function
