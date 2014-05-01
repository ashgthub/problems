import unittest

from euler_problem_20 import factorial_digit_sum

class TestEulerProblem20(unittest.TestCase):

	def test_char_input(self):
		self.assertRaises(Exception,factorial_digit_sum,'blah')

	def test_factorial_digit_sum_100(self):
		sum = factorial_digit_sum(100)
		self.assertEqual(sum,648)

	def test_factorial_digit_sum(self):
		sum = factorial_digit_sum(10)
		self.assertEqual(sum,27)

	def test_factorial_digit_sum_default_value(self):
		sum = factorial_digit_sum()
		self.assertEqual(sum,648)

if __name__ == '__main__':
    unittest.main()