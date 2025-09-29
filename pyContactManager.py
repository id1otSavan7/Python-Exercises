import os
filepath = "C:\\Users\\Lance\\Documents\\Programming Projects\\Python Project"
contacts = []

def checkIfContactsExist():
    if os.path.exists(f"{filepath}\\contacts.txt"):
        print("File already exists...")
    else:
        open(f"{filepath}\\contacts.txt", 'x')
        print("File was created successfully...")

def checkFilePath():
    new_filePath = filepath + "\\contacts.txt"
    if os.path.exists(new_filePath):
        return new_filePath
    else:
        checkIfContactsExist()

def getDataFromContacts():
    contacts.clear()
    with open(checkFilePath(), 'r') as list:
        lists = list.readlines()
        for names in lists:
            contacts.append(names)  

def viewContacts():
    getDataFromContacts()
    print("Existing Contacts: ")
    for i in range(len(contacts)):
        print(f"{i+1}. {contacts[i].replace('\n','')}")

def addRecipientToContacts():
    getDataFromContacts()
    msg =''
    print("Enter Recipient Name: ")
    name = input(">> ").strip().title()
    print("Enter Recipient Phone Number: ")
    phoneNumber = input(">> ")

    try:
        if name and phoneNumber:
            if name not in contacts:
                with open(checkFilePath(), 'a') as new_list:
                    new_list.write(f"Name: {name}, Phone: {phoneNumber}\n")
                    print("[ADD] Recipient successfully added to your contacts...")
                    raise ValueError         
        else:
            msg = 'Invalid input or input left empty...'
            raise ValueError    
    except ValueError:
            print(f"[ADD] {msg}")

def searchRecipientFromContacts():
    getDataFromContacts()
    choice = ['Recipient Name', 'Phone Number']
    print("\nChoose which one will you want to search: ")
    for i in range(len(choice)):
        print(f"{i+1}. {choice[i]}")
    user_choice = str(input(">> "))

    dis_query = []
    try:
        if user_choice == '1':
            print("Enter recipient name: ")
            name = input(">> ").strip().title()
            print(f"\nSearched for \"{name}\":")
            for contact in contacts:
                if f'Name: {name}' in contact:
                    dis_query.append(contact)
            if dis_query:
                for i in range(len(dis_query)):
                    print(f"{i+1}. {dis_query[i].replace('\n', '')}")
                print('\n')
            else:
                print(f"{name} seems like does not exist in your contacts...\n")

        elif user_choice == '2': 
            print("Enter recipient Phone Number: ")
            phoneNumber = str(input('>> '))

            print(f"Searched for \"{phoneNumber}\":")
            for contact in contacts:
                if f', Phone: {phoneNumber}' in contact:
                    dis_query.append(contact)
            
            if dis_query:
                for i in range(len(dis_query)):
                    print(f"{i+1}. {dis_query[i].replace('\n', '')}")
                print('\n')
            else:
                print(f"No Phone Number \'{phoneNumber}\' exist like this in your contacts...\n")

        else:
            print("[SRC] Invalid choice detected...")
            raise ValueError

    except ValueError:
        print("[SRC] Something went wrong...")
        
def updateContactInformation():
    getDataFromContacts()

    viewContacts()
    print("Choose the corresponding number of which data you want to update: ")
    user_prompt = input(">> ")
    user_prompt = int(user_prompt)

    print(f"[UPD] >> Changing: {contacts[user_prompt-1]}")
    print("Enter Recipient\'s new Name: ")
    new_name = input(">> ")
    print("Enter Recipient\'s new Phone Number: ")
    new_phoneNumber = input(">> ")

    contacts[user_prompt-1] = f"Name: {new_name}, Phone:{new_phoneNumber}\n"
    print(contacts)

    modified_contacts = []
    #Delete entire list in the text file
    with open(checkFilePath(), 'w') as text:
        text.write('')

    #Rewrite data from contacts to modified contacts
    for data in contacts:
        modified_contacts.append(data)

    #Restore modified data from modified contacts to the text file
    with open(checkFilePath(), 'w') as list:
        for data in modified_contacts:
            list.write(data)

def deleteContactInformation():
    getDataFromContacts()
    
    viewContacts() 
    print("Choose the corresponding number of which data you want to delete: ")
    user_prompt = input('>> ')
    user_prompt = int(user_prompt)

    print(f"Data {user_prompt}. {contacts[user_prompt-1]} was removed...")
    contacts.pop(user_prompt - 1)
    
    modified_contacts = []
    #Delete entire list in the text file
    with open(checkFilePath(), 'w') as text:
        text.write('')

    #Rewrite data from contacts to modified contacts
    for data in contacts:
        modified_contacts.append(data)

    #Restore modified data from modified contacts to the text file
    with open(checkFilePath(), 'w') as list:
        for data in modified_contacts:
            list.write(data)
    


if __name__ == "__main__":
    operation = ["Add Contact", "Search Contact", "Update Contact", "Delete Contact", "View All Contacts"]
    checkIfContactsExist()
    getDataFromContacts()

    while (True):
        print("Contact Manager v2\n")
        print("Please choose the corresponding number on which action will be executed:")
        for i in range(len(operation)):
            print(f"{i+1}. {operation[i]}")
        print("Enter choice: ")
        user_input = input(">> ")

        match user_input:
            case '1': #Add Recipients
                addRecipientToContacts()
            case '2': #Search Contact
                searchRecipientFromContacts()
            case '3': #Update Contact
                updateContactInformation()
            
            case '4': #Delete Contact
                deleteContactInformation()
            
            case '5': #View All Contacts
                viewContacts()

            case 'quit':
                print("Terminating program execution code...")
                break
