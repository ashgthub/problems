
import unittest

from euler_problem_2 import fibonacci_even_seq_sum

class TestEulerProblem2(unittest.TestCase):

	def test_char_input(self):
		self.assertRaises(ValueError,fibonacci_even_seq_sum,'blah')

	def test_even_sum(self):
		sum = fibonacci_even_seq_sum(50)
		self.assertEqual(sum,4613732)

	def test_even_sum_less_than_32(self):
		sum = fibonacci_even_seq_sum(30)
		self.assertNotEqual(sum,4613732)
 
if __name__ == '__main__':
    unittest.main()
