import json

# Contact book data storage
contact_book = {}

def save_contacts():
    """Save contacts to a file"""
    with open("contacts.json", "w") as file:
        json.dump(contact_book, file)

def load_contacts():
    """Load contacts from a file"""
    global contact_book
    try:
        with open("contacts.json", "r") as file:
            contact_book = json.load(file)
    except FileNotFoundError:
        contact_book = {}

# Add a new contact
def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter name: ").strip()
    if name in contact_book:
        print("Contact already exists!")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email (optional): ").strip()
    address = input("Enter address (optional): ").strip()
    contact_book[name] = {"phone": phone, "email": email, "address": address}
    save_contacts()
    print(f"Contact '{name}' added successfully!\n")

# View all contacts
def view_contacts():
    print("\n--- Contact List ---")
    if not contact_book:
        print("No contacts found!\n")
        return
    for name, details in contact_book.items():
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        if details['email']:
            print(f"Email: {details['email']}")
        if details['address']:
            print(f"Address: {details['address']}")
        print("-")

# Search for a contact
def search_contact():
    print("\n--- Search Contact ---")
    query = input("Enter name, phone number, or address to search: ").strip()
    results = {name: details for name, details in contact_book.items() if query.lower() in name.lower() or query in details['phone'] or query.lower() in details['address'].lower()}
    if not results:
        print("No matching contacts found!\n")
        return
    print("Matching contacts:")
    for name, details in results.items():
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        if details['email']:
            print(f"Email: {details['email']}")
        if details['address']:
            print(f"Address: {details['address']}")
        print("-")

# Update a contact
def update_contact():
    print("\n--- Update Contact ---")
    name = input("Enter the name of the contact to update: ").strip()
    if name not in contact_book:
        print("Contact not found!\n")
        return
    print("Leave a field blank to keep the current value.")
    phone = input(f"Enter new phone number (current: {contact_book[name]['phone']}): ").strip()
    email = input(f"Enter new email (current: {contact_book[name]['email']}): ").strip()
    address = input(f"Enter new address (current: {contact_book[name]['address']}): ").strip()
    if phone:
        contact_book[name]['phone'] = phone
    if email:
        contact_book[name]['email'] = email
    if address:
        contact_book[name]['address'] = address
    save_contacts()
    print(f"Contact '{name}' updated successfully!\n")

# Delete a contact
def delete_contact():
    print("\n--- Delete Contact ---")
    name = input("Enter the name of the contact to delete: ").strip()
    if name not in contact_book:
        print("Contact not found!\n")
        return
    del contact_book[name]
    save_contacts()
    print(f"Contact '{name}' deleted successfully!\n")

# Main menu
def main_menu():
    load_contacts()
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again!\n")

if __name__ == "__main__":
    main_menu()