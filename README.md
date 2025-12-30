Contact Management System

A Python-based application to store, update, delete, and manage contact information.

Project Description

The Contact Management System is a Python console application designed to manage personal and professional contacts with ease. It supports full CRUD operations, search, CSV export, statistics, and file-based data storage.

It uses:

Dictionaries for storing contact information

Functions to modularize features

JSON & CSV for data persistence and export

Input validation for phone and email format

Features

Feature	                          Description

Add Contact	                      Stores a new contact with name, phone, email, address & group

Search	                          Search by full/partial name

Update	                          Modify existing contact fields

Delete	                          Remove a contact permanently

Display                           All	View all stored contacts

Save to File	                    Save all contacts to contacts.json

Backup	                          Create timestamped backup files

Export to CSV                     Generate contacts.csv for Excel import

Statistics	                      View contacts count by group

Persistent Storage	              Data remains saved between sessions

Project Structure
week3-contact-manager/
│── contacts_manager.py        # Main program
│── contacts_data.json         # Data file (auto created)
│── test_contacts.py           # Unit tests
│── README.md                  # Documentation
│── requirements.txt           # Dependencies
└── .gitignore

Requirements & Installation
Install Python

Download from ➝ https://www.python.org/downloads/

Make sure to check:

Add Python to PATH


Verify installation:

python --version

Install Dependencies

If using requirements.txt:

pip install -r requirements.txt

How to Run the Program

Open terminal inside project folder:

python contacts_manager.py


You will see a menu:

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

Running Tests

The project includes automated tests using unittest.

Run all tests:

python -m unittest test_contacts.py

Technical Approach

Used Python dictionaries to store contact data
Applied regex for validating email input
Used JSON & CSV for persistence
Modular design using functions for each task
User-friendly menu-driven interface

Sample JSON Storage Format
{
  "Ravi": {
    "phone": "9876543210",
    "email": "ravi@mail.com",
    "address": "Hyderabad",
    "group": "Friends",
    "created_at": "2025-01-10T10:20:30",
    "updated_at": "2025-01-10T10:20:30"
  }
}

Sample Test Case Scenarios

Test Type	                          Expected Behavior
Invalid Phone	                      Shows error until correct 10-digit number is given
Invalid Email	                      Warns and stores blank value
Duplicate Contact	                  Prevents insertion
Backup	                            Creates file with timestamp
Export CSV	                        Generates contacts.csv file
