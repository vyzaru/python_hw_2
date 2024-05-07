import unittest
import time
import sys
from factorial_test import factorial

class TestFactorial(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.start_time = time.time()

    @classmethod
    def tearDownClass(cls):
        end_time = time.time()
        execution_time = end_time - cls.start_time
        print(f"Время выполнения всех тестов: {execution_time:.6f} сек")

    def test_positive(self):
        self.assertEqual(factorial(4), 24)

    def test_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_float(self):
        with self.assertRaises(TypeError):
            factorial(1.01)

    def test_out_of_range(self):
        with self.assertRaises(ValueError):
            factorial(10000)

    def test_maxsize(self):
        with self.assertRaises(ValueError):
            factorial(sys.maxsize)

if __name__ == "__main__":
    unittest.main()
