#! /usr/bin/python

from timing_decorator import calculate_timing

#This will save the results from sub-calls during recusrion
factorial_table = {}

@calculate_timing
def factorial_digit_sum(number=100):
	"""
	This method calculates the sum of all the digits of
	the factorial of a number.
	For e.g, the factorial of 10 = 3628800. The sum of the
	digits is 27.

	:param number: The number whose factorial and sum of all 
				   the digits of the factorial to be calculated.
				   The default value is 100.
	
	"""
	#Get the factorial of the number
	try:
		fact_number = __factorial(number)
	except Exception,e:
		raise(e)
	else:
		return sum([int(fact_digit) for fact_digit in str(fact_number)])

def __factorial(number):
	"""
	This method calculates the Factorial of a given number using
	resursion.The results of sub calls from the recursive calls are 
	saved in the dict to avoid recomputation.

	:param number: The number whose factorial is be calculated.
	"""
	if number <= 2:
		return number
	#check if we have already calculated the factorial
	if number in factorial_table:
		return factorial_table[number]

	factorial_table[number] =  __factorial(number-1) * number

	return factorial_table[number]


def main():
	fact_digit_sum = factorial_digit_sum(100)
	print 'The sum of the digits in the number 100! is %s ' % (fact_digit_sum,)

if __name__ == '__main__':
	main()