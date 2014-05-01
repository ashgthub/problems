
import unittest
import math
from euler_problem_13 import calculate_big_sum

class TestEulerProblem13(unittest.TestCase):

	def setUp(self):
		self.sum = calculate_big_sum('big_num.txt')
 
	def test_file_open(self):
		self.assertRaises(IOError,calculate_big_sum,'foo.txt')
    
	def test_sum_length(self):
		sum_len = int(math.log10(self.sum))+1
		self.assertEqual(sum_len,10)

	def test_sum(self):
		self.assertEqual(self.sum,5537376230)

 
if __name__ == '__main__':
    unittest.main()