# ------------------------------------------------------------------------------- #
# Title: Test Data Classes Module
# # Description: A collection of tests for the presentation classes module
# ChangeLog: (Who, When, What)
# JSpencer,6.18.2025,Created Script
# ------------------------------------------------------------------------------- #

import unittest
from unittest.mock import patch
from presentation_classes import IO
from data_classes import Employee

class TestIO(unittest.TestCase):
    def setUp(self):
        self.employee_data = []

    def test_input_menu_choice(self):
        with patch('builtins.input', return_value='2'):
            choice = IO.input_menu_choice()
            self.assertEqual(choice, 2)

    def test_input_employee_data(self):
        with patch('builtins.input', side_effect=["John", "Doe", "2030-01-01", 5]):
            IO.input_employee_data(employee_data=self.employee_data, employee_type=Employee)
            self.assertEqual(len(self.employee_data), 2)
            self.assertEqual(self.employee_data[0]["FirstName"], "John")
            self.assertEqual(self.employee_data[0]["LastName"], "Doe")
            self.assertEqual(self.employee_data[0]["ReviewDate"], "2030-01-01")
            self.assertEqual(self.employee_data[0]["ReviewRating"], 5)
        with patch('builtins.input', side_effect=["Alice", "1234", "2030-01-01", 4]):
            IO.input_employee_data(employee_data=self.employee_data, employee_type=Employee)
            self.assertEqual(len(self.employee_data), 1)

if __name__ == '__main__':
    unittest.main()