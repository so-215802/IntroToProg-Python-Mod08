# ------------------------------------------------------------------------------- #
# Title: Test Data Classes Module
# # Description: A collection of tests for the data classes module
# ChangeLog: (Who, When, What)
# Seth Overbay, 06/16/2025, Created Script
# ------------------------------------------------------------------------------- #

import unittest
from data_classes import Person, Employee
from datetime import date

class TestPerson(unittest.TestCase):

    def test_person_init(self):  # Tests the constructor
        person = Person("John", "Doe")
        self.assertEqual(person.first_name, "John")
        self.assertEqual(person.last_name, "Doe")

    def test_person_invalid_name(self):  # Test the first and last name validations
        with self.assertRaises(ValueError):
            person = Person("123", "Doe")
        with self.assertRaises(ValueError):
            person = Person("John", "123")

    def test_person_str(self):  # Tests the __str__() magic method
        person = Person("John", "Doe")
        self.assertEqual(str(person), "John,Doe")

class TestEmployee(unittest.TestCase):

    def test_employee_init(self):  # Tests the constructor
        employee = Employee("John", "Doe", "2030-01-01", 5)
        self.assertEqual(employee.first_name, "John")
        self.assertEqual(employee.last_name, "Doe")
        self.assertEqual(employee.review_date, "2030-01-01")
        self.assertEqual(employee.review_rating, 5)

    def test_employee_rating_type(self):  # Tests validation for review rating attribute
        with self.assertRaises(ValueError):
            employee = Employee("John", "Doe", "2030-01-01", 8)

    def test_employee_str(self):
        employee = Employee("John", "Doe", "2030-01-01", 5)  # Tests the __str__() magic method
        self.assertEqual(str(employee), "John,Doe,2030-01-01,5")

if __name__ == '__main__':
    unittest.main()