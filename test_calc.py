import unittest
import calculator

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(10,5),15)
        self.assertEqual(calculator.add(10,2.5),12.5)

    def test_sub(self):
        self.assertEqual(calculator.substract(10,5),5)
        self.assertEqual(calculator.substract(10,1.1),8.9)

    def test_mul(self):
        self.assertEqual(calculator.multiply(10,5),50)
        self.assertEqual(calculator.multiply(2.2,2),4.4)
    
    def test_div(self):
        self.assertEqual(calculator.divide(10,5), 2) 
        self.assertEqual(calculator.divide(5,2),2.5)
        with self.assertRaises(ValueError):
            calculator.divide(2,0)

if __name__ == "__main__":
    unittest.main()