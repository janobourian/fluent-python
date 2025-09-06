"""
To execute the tests, run the following command in the terminal:
python -m unittest discover -s test_unittest -p "test_*.py"

other options:
(Remember to add the -v flag for verbose output)
(Remember to run from the root directory of the project)
(Remember to add `__init__.py` files to the directories to be recognized as packages)
python -m unittest test_unittest.test_fibo_function -v
"""

from functions_to_test.fibo import fibo
import unittest

class TestFiboFunction(unittest.TestCase):
    
    def test_fibo(self):
        self.assertEqual(fibo(0), 0)
    
    def test_fibo_negative(self):
        self.assertEqual(fibo(-1), 0)
    
    def test_fibo_one(self):
        self.assertEqual(fibo(1), 1)
    
    def test_fibo_two(self):
        self.assertEqual(fibo(2), 1)

    def test_fibo_three(self):
        self.assertEqual(fibo(3), 2)

    def test_fibo_three_hundred(self):
        self.assertEqual(fibo(300), 222232244629420445529739893461909967206666939096499764990979600)

if __name__ == '__main__':
    unittest.main()