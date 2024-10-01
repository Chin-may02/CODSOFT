contacts = {}

while True:
    print('\nContacts')
    print('1. Add Contact')
    print('2. View Contact List')
    print('3. Search Contact')
    print('4. Update Contact')
    print('5. Delete Contact')
    print('6. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        name = input('Enter name: ')
        if name in contacts:
            print(f'Contact name {name} already exists!')
        else:
            storename = input('Enter store name: ')
            phonenumber = input('Enter the contact number: ')
            email = input('Enter the email id: ')
            address = input('Enter the address: ')
            contacts[name] = {
                'StoreName': storename,
                'PhoneNumber': phonenumber,
                'Email-Id': email,
                'Address': address
            }
            print(f'Contact name {name} has been created successfully!')

    elif choice == '2':
        if contacts:
            print('\nContact List:')
            for name, details in contacts.items():
                print(f"Name: {name}, Store: {details['StoreName']}, Phone: {details['PhoneNumber']}, Email: {details['Email-Id']}, Address: {details['Address']}")
        else:
            print('No contacts found.')

    elif choice == '3':
        name = input('Enter name to search: ')
        if name in contacts:
            details = contacts[name]
            print(f"Name: {name}, Store: {details['StoreName']}, Phone: {details['PhoneNumber']}, Email: {details['Email-Id']}, Address: {details['Address']}")
        else:
            print('Contact not found!')

    elif choice == '4':
        name = input('Enter name to be updated: ')
        if name in contacts:
            storename = input('Enter updated store name: ')
            phonenumber = input('Enter the updated contact number: ')
            email = input('Enter the email to be updated: ')
            address = input('Enter the updated address: ')
            contacts[name] = {
                'StoreName': storename,
                'PhoneNumber': phonenumber,
                'Email-Id': email,
                'Address': address
            }
            print(f'Contact name {name} has been updated successfully!')
        else:
            print('Contact not found!')

    elif choice == '5':
        name = input('Enter contact to be deleted: ')
        if name in contacts:
            del contacts[name]
            print(f'Contact name {name} has been deleted successfully!')
        else:
            print('Contact not found!')

    elif choice == '6':
        print('Thank you for using the contact book!')
        break

    else:
        print('Invalid Input')
