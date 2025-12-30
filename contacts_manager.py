# Contact Management System

import json
import re
from datetime import datetime
import csv

contacts={}

def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10

def validate_email(email):
    pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def add_contact():
    name=input("Enter Name:")
    if name in contacts:
        print("Contact already exists!")
        return
    phone=input("Enter Phone Number (10 digits): ")
    while not validate_phone(phone):
        print("Invalid phone number. Please enter a 10-digit number.")
        phone=input("Enter Phone Number (10 digits): ")
        
    email=input("Enter Email: ")
    if email and not validate_email(email):
        print("Invalid email format.")
        email=""
        
    address=input("Enter Address: ")
    group=input("Enter Group (Family/Friends/Work/Others): ")
    
    contacts[name]={
        'phone':phone,
        'email':email,
        'address':address,
        'group':group,
        'created_at':datetime.now().isoformat(),
        'updated_at':datetime.now().isoformat()
    }
    print(f"Contact {name} added successfully!")
    return contacts
    
def search_contact():
    key=input("Enter name or partial name to search: ").lower()
    print("="*30)
    print("\n Search Results: ")
    print("="*30)
    for name,info in contacts.items():
        if key in name.lower():
            print(f"Name: {name}")
            for k,v in info.items():
                print(f"{k.title()}: {v}")
    print()

def update_contact():
    name=input("Enter the name to update: ")
    if name not in contacts:
        print("Contact not found!")
        return
    print("Leave field empty to keep old value!!")
    phone=input(f"Enter new phone number ({contacts[name]['phone']}): ")
    if phone and validate_phone(phone):
        contacts[name]['phone']=phone
    email=input(f"Enter new email ({contacts[name]['email']}): ")
    if email and validate_email(email):
        contacts[name]['email']=email
    address=input(f"Enter new address ({contacts[name]['address']}): ")
    if address:
        contacts[name]['address']=address
    group=input(f"Enter new group ({contacts[name]['group']}): ")
    if group:
        contacts[name]['group']=group
    print("="*30)
    print("Contact updated successfully!")
    print("="*30)
    
def delete_contact():
    name=input("Enter name to delete: ")
    if name not in contacts:
        print("Contact not found!")
        return
    confirm=input(f"Are you sure you want to delete '{name}'? (y/n)").lower()
    if confirm=='y':
        del contacts[name]
        print("="*30)
        print("Contact deleted!")
        print("="*30)
    else:
        print("Deletion cancelled!")
    print()

def display_all():
    if not contacts:
        print("No contacts to display!")
        return
    print("="*30)
    print("="*30)
    print("\n All contacts: ")
    print("="*30)
    print("="*30)
    for name,info in contacts.items():
        print(f"\nName: {name}")
        for k, v in info.items():
            print(f"{k.title()}: {v}")
    print()

# FILE OPERATIONS

def save_to_file():
    with open("contacts.json","w") as f:
        json.dump(contacts, f, indent=4)
    print("Contacts saved to contacts.json!\n")

def load_from_file():
    global contacts
    try:
        with open("contacts.json", "r") as f:
            contacts=json.load(f)
        print("="*30)
        print("Contacts loaded successfully!\n")
        print("="*30)
    except FileNotFoundError:
        print("No saved file found.\n")

def backup():
    filename=f"contacts_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w") as f:
        json.dump(contacts, f, indent=4)
    print("="*30)
    print(f"Backup saved as {filename}\n")
    print("="*30)
    
    
# ADVANCED FEATURES

def export_to_csv():
    with open("contacts.csv", "w", newline="") as f:
        writer=csv.writer(f)
        writer.writerow(["Name", "Phone", "Email", "Address", "Group"])
        for name,info in contacts.items():
            writer.writerow([name,info["phone"],info["email"],info["address"], info['group']])
    print("="*30)
    print("Exported to contacts.csv\n")
    print("="*30)
    

def statistics():
    print("="*30)
    print("\nContact Statistics: ")
    print("="*30)
    print(f" Total Contacts: {len(contacts)}")
    groups={}
    for info in contacts.values():
        group=info["group"]
        groups[group]=groups.get(group,0)+1
    print("="*30)
    print("Contacts by Groups: ")
    print("="*30)
    for g,c in groups.items():
        print(f" {g}: {c}")
    print()

# USER MENU

def main_menu():
    load_from_file()
    
    while True:
        print("""
==========CONTACT MANAGER===========
1. Add Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. Display All Contacts
6. Save Contacts to File
7. Backup Contacts
8. Export to CSV
9. Statistics
0. Exit
===================================
              """)
        choice=input("Enter choice:")
        if choice=='1':
            add_contact()
        elif choice=='2':
            search_contact()
        elif choice=='3':
            update_contact()
        elif choice=='4':
            delete_contact()
        elif choice=='5':
            display_all()
        elif choice=='6':
            save_to_file()
        elif choice=='7':
            backup()
        elif choice=='8':
            export_to_csv()
        elif choice=='9':
            statistics()
        elif choice=='0':
            save_to_file()
            print("Exiting program!")
            print("="*35)
            print("Thank you for using the program!")
            print("="*35)
            break
        else:
            print("Invalid choice! Enter again.!\n")

main_menu()