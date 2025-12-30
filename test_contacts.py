import unittest
from unittest.mock import patch
from contacts_manager import (
    validate_phone, validate_email, add_contact,
    update_contact, delete_contact, contacts
)

class TestContactManager(unittest.TestCase):

    def setUp(self):
        """Reset contacts before each test"""
        contacts.clear()

    # ---------- Validation Tests ----------
    def test_validate_phone(self):
        self.assertTrue(validate_phone("9876543210"))
        self.assertFalse(validate_phone("12345"))
        self.assertFalse(validate_phone("abc1234567"))

    def test_validate_email(self):
        self.assertTrue(validate_email("test@example.com"))
        self.assertFalse(validate_email("invalid.com"))
        self.assertFalse(validate_email("abc@.in"))

    # ---------- Add Contact ----------
    @patch("builtins.input", side_effect=["Ravi", "9876543210", "ravi@mail.com", "Hyd", "Friends"])
    def test_add_contact(self, mock_input):
        add_contact()
        self.assertIn("Ravi", contacts)
        self.assertEqual(contacts["Ravi"]["group"], "Friends")

    # ---------- Update Contact ----------
    @patch("builtins.input", side_effect=[
        "Ravi", "9876543210", "ravi@mail.com", "Hyd", "Work"  # add first
    ])
    def test_update_contact(self, mock_input1):
        add_contact()  # Add Ravi first

        with patch("builtins.input", side_effect=["Ravi", "9999999999", "", "Bangalore", "Friends"]):
            update_contact()

        self.assertEqual(contacts["Ravi"]["phone"], "9999999999")
        self.assertEqual(contacts["Ravi"]["address"], "Bangalore")
        self.assertEqual(contacts["Ravi"]["group"], "Friends")

    # ---------- Delete Contact ----------
    @patch("builtins.input", side_effect=["Ravi", "9876543210", "ravi@mail.com", "Hyd", "Work"])
    def test_delete_contact(self, mock_add):
        add_contact()
        with patch("builtins.input", side_effect=["Ravi", "y"]):
            delete_contact()
        self.assertNotIn("Ravi", contacts)

if __name__ == "__main__":
    unittest.main()
