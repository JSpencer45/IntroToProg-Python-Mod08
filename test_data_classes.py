# ------------------------------------------------------------------------------- #
# Title: Test Data Classes Module
# # Description: A collection of tests for the data classes module
# ChangeLog: (Who, When, What)
# JSpencer,6.18.2025,Created Script
# ------------------------------------------------------------------------------- #

import unittest
from data_classes import Person
from data_classes import Employee

class TestPerson(unittest.TestCase):
    def test_person_init(self):
        person = Person("John", "Johnson")
        self.assertEqual(person.first_name, "John")
        self.assertEqual(person.last_name, "Johnson")

    def test_person_invalid_name(self): # Test the first and last name validations
        with self.assertRaises(ValueError):
            person = Person("123", "Johnson")
        with self.assertRaises(ValueError):
            person = Person("John", "123")

    def test_person_str(self): # Tests the __str__() magic method
        person = Person("John", "Johnson")
        self.assertEqual(str(person), "John,Johnson")

class TestEmployee(unittest.TestCase):
    def test_employee_init(self):  # Tests the constructor
        employee = Employee("John", "Johnson", "1111-11-11", 5)
        self.assertEqual(employee.first_name, "John")
        self.assertEqual(employee.last_name, "Johnson")
        self.assertEqual(employee.review_date, "1111-11-11")
        self.assertEqual(employee.review_rating, 5)

    def test_employee_invalid_review_date(self): # Test the review date validation
        with self.assertRaises(ValueError):
            employee = Employee("John", "Johnson", "abcd", 5)

    def test_employee_invalid_review_rating(self): # Test the review rating validation
        with self.assertRaises(ValueError):
            employee = Employee("John", "Johnson", "1111-11-11", "a")

    def test_employee_str(self):
        employee = Employee("John", "Johnson", "1111-11-11", 5)
        self.assertEqual(str(employee), "John,Johnson,1111-11-11,5")

if __name__ == '__main__':
    unittest.main()