import json


filename = "contacts.json"


def load_contacts():
    try:
        with open(filename, "r") as file:
            return json.load(file) 
    except FileNotFoundError:
        return []  


def save_contacts(contacts):
    with open(filename, "w") as file:
        json.dump(contacts, file, indent=4)  


def add_contact(name, phone):
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone}) 
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")


def display_contacts():
    contacts = load_contacts()
    if contacts:
        print("\nContact List:")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} - {contact['phone']}")
    else:
        print("No contacts found.")


def delete_contact():
    contacts = load_contacts()
    display_contacts() 
    if contacts:
        try:
            contact_index = int(input("Enter the number of the contact to delete: ")) - 1
            if 0 <= contact_index < len(contacts):
                removed_contact = contacts.pop(contact_index)
                save_contacts(contacts)
                print(f"Contact '{removed_contact['name']}' deleted successfully.")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Please enter a valid number.")


def rename_contact():
    contacts = load_contacts()
    display_contacts()  
    if contacts:
        try:
            contact_index = int(input("Enter the number of the contact to rename: ")) - 1
            if 0 <= contact_index < len(contacts):
                new_name = input("Enter the new name for the contact: ")
                contacts[contact_index]['name'] = new_name
                save_contacts(contacts)
                print(f"Contact name updated to '{new_name}' successfully.")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Please enter a valid number.")


while True:
    print("\n--- Simple Contact Manager ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Rename Contact")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        add_contact(name, phone)
    elif choice == "2":
        display_contacts()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        rename_contact()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
