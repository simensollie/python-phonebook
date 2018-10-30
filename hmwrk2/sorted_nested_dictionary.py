def listSurname():
    orderedSurname = dict(sorted(phonebook.items(), key=lambda x: x[1]['surname']))
    print('Phonebook ordered by surname:')

    for pNumber, pInfo in orderedSurname.items():
        print('\nPerson number:', pNumber)
        for key in pInfo:
            print(key + ':', pInfo[key])
            # end of function listSurname