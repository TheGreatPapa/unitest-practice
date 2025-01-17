import unittest
from employee import Employee
from unittest.mock import patch

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp_1 = Employee('Corey', 'Chafer',50000)
        self.emp_2 = Employee('Jane', 'Doe',20000)

    def tearDown(self):
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, "corey.chafer@email.com")
        self.assertEqual(self.emp_2.email, "jane.doe@email.com")

        self.emp_1.first = "Luca"
        self.emp_2.first = "Viktor"

        self.assertEqual(self.emp_1.email, "luca.chafer@email.com")
        self.assertEqual(self.emp_2.email, "viktor.doe@email.com")
        
    def test_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay,52500)
        self.assertEqual(self.emp_2.pay,21000)

    def test_name(self):
        self.assertEqual(self.emp_1.first, 'Corey')
        self.assertEqual(self.emp_2.first, 'Jane')
        self.assertEqual(self.emp_1.last, 'Chafer')
        self.assertEqual(self.emp_2.last, 'Doe')
    
    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Corey Chafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Doe')

        self.emp_1.first = "Luca"
        self.emp_2.first = "Viktor"

        self.assertEqual(self.emp_1.fullname, 'Luca Chafer')
        self.assertEqual(self.emp_2.fullname, 'Viktor Doe')

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Chafer/May')
            self.assertEqual(schedule,'Success')

            mocked_get.return_value.ok = False
            

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Doe/June')
            self.assertEqual(schedule,'Bad response!')

if __name__ == "__main__":
    unittest.main()
