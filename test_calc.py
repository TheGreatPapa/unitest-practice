import unittest
import calculator

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(10,5),15)

    def test_sub(self):
        self.assertEqual(calculator.substract(10,5),5)

    def test_mul(self):
        self.assertEqual(calculator.multiply(10,5),50)
    
    def test_div(self):
        self.assertEqual(calculator.divide(10,5), 2) 
        self.assertRaises(ZeroDivisionError, calculator.divide, 2, 0)

if __name__ == "__main__":
    unittest.main()