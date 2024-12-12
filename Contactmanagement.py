import json
import os

# Define the filename for storing contacts
CONTACTS_FILE = "contacts.json"

# Load contacts from the file
def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return {}
    with open(CONTACTS_FILE, "r") as file:
        return json.load(file)

# Save contacts to the file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    if name in contacts:
        print("A contact with this name already exists.")
    else:
        contacts[name] = {"phone": phone, "email": email}
        print(f"Contact '{name}' added successfully.")
    return contacts

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        print("\nContacts List:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    print()

# Edit an existing contact
def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ").strip()
    if name not in contacts:
        print("Contact not found.")
    else:
        print(f"Editing contact '{name}':")
        phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ").strip()
        email = input(f"Enter new email address (current: {contacts[name]['email']}): ").strip()

        contacts[name]['phone'] = phone or contacts[name]['phone']
        contacts[name]['email'] = email or contacts[name]['email']
        print(f"Contact '{name}' updated successfully.")
    return contacts

# Delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    if name not in contacts:
        print("Contact not found.")
    else:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    return contacts

# Main function
def main():
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            contacts = add_contact(contacts)
            save_contacts(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            contacts = edit_contact(contacts)
            save_contacts(contacts)
        elif choice == "4":
            contacts = delete_contact(contacts)
            save_contacts(contacts)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
