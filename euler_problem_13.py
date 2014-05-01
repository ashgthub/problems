#! /usr/bin/python

from timing_decorator import calculate_timing

@calculate_timing
def calculate_big_sum(big_num_file):
	"""
	This method reads big numbers from the passed in input file
	which contains one-hundred 50-digit numbers and calculates
	the sum of the numbers. The return value is the first ten 
	digits of the sum.
	
	:param big_num_file: A file name that contains the big numbers.
	"""
	with open(big_num_file, 'r') as num_file:
		big_sum = 0
		for num in num_file:
			big_sum = big_sum + long(num.strip())

	return long(str(big_sum)[:10])


def main():
	input_file = 'big_num.txt'
	try:
		sum = calculate_big_sum(input_file)
		print 'The first ten digits of the sum is %s ' % (sum,)
	except IOError:
		print 'File Not Found: A input file %s is required to run this program' % (input_file,)
		

if __name__ == '__main__':
    main()
 
