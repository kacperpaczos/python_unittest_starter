# test_math_functions.py

import unittest
from package.math_functions import *

# Define class to test the program
class TestMathFunctions(unittest.TestCase):
	# Function to test addition function
	def test_addition(self):
		result = addition(2, 2)
		self.assertEqual(result, 4)
		
	# Function to test addition function
	def test_subtraction(self):
		result = subtraction(4, 2)
		self.assertEqual(result, 2)
		
# Function to test addition function
	def test_multiplication(self):
		result = multiplication(2, 3)
		self.assertEqual(result, 6)
		
	# Function to test addition function
	def test_division(self):
		result = division(4, 2)
		self.assertEqual(result, 2)

if __name__ == '__main__':
	unittest.main()
