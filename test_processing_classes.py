# ------------------------------------------------------------------------------- #
# Title: Test Data Classes Module
# # Description: A collection of tests for the processing classes module
# ChangeLog: (Who, When, What)
# JSpencer,6.18.2025,Created Script
# ------------------------------------------------------------------------------- #
import json
import tempfile
import unittest
import data_classes as data

from processing_classes import FileProcessor

class TestFileProcessor(unittest.TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.file_data = None

    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name
        self.employee_data = []
    def tearDown(self):
        self.temp_file.close()
    def test_read_employee_data_from_file(self):
        sample_data = [
            {"FirstName": "John", "LastName": "Doe", "ReviewDate": "2030-01-01", "ReviewRating": 5},
        ]
        with open(self.temp_file_name, "w") as temp_file:
            json.dump(sample_data, temp_file)

        employee_data = FileProcessor.read_employee_data_from_file(self.temp_file_name,
                                                                   self.employee_data,
                                                                   data.Employee)
        self.assertEqual(len(sample_data), len(employee_data))

        self.assertEqual(self.employee_data[0].first_name,"John")
        self.assertEqual(self.employee_data[0].last_name,"Doe")
        self.assertEqual(self.employee_data[0].review_date,"2030-01-01")
        self.assertEqual(self.employee_data[0].review_rating,5)

    def test_write_employee_data_to_file(self):
        sample_data = [
            data.Employee("John", "Johnson", "2030-01-01", 5),
            data.Employee("Will", "Williams", "2030-01-01", 2)
        ]
        FileProcessor.write_employee_data_to_file(self.temp_file_name, sample_data)
        with open(self.temp_file_name, "r") as file:
            file_data = json.load(file)

        self.assertEqual(len(file_data), len(sample_data))
        self.assertEqual(self.file_data[0].FirstName,"John")
        self.assertEqual(self.file_data[0].LastName,"Johnson")
        self.assertEqual(self.file_data[0].review_date,"2030-01-01")
        self.assertEqual(self.file_data[0].review_rating,5)
        self.assertEqual(self.file_data[1].FirstName, "Will")
        self.assertEqual(self.file_data[1].LastName, "Williams")
        self.assertEqual(self.file_data[1].review_date,"2030-01-01")
        self.assertEqual(self.file_data[1].review_rating,2)

if __name__ == '__main__':
    unittest.main()