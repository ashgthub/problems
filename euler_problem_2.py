#! /usr/bin/python
import sys
import os
from timing_decorator import calculate_timing

#The limit to stop while calculating the sum
FIBO_EVEN_SUM_MAX = 4000000

@calculate_timing
def fibonacci_even_seq_sum(number):
    """
    This method genetates the fibonacci sequence of the 
    given number and caculates the sum of all the even-valued
    terms whose values do not exceed four million.
    
    :param number: The number whose fibonacci sequence and sum of
                    even-valued terms to be calculated.
    """

    try:
        number = int(number)
    except:
        raise ValueError
    else:    
        fibo_seq_values = [0,1]
        fibo_even_sum = 0
        for num in xrange(2,number+1):
            fibo_sum = fibo_seq_values[num-1] + fibo_seq_values[num-2]
            fibo_seq_values.append(fibo_sum)
            if fibo_sum & 1 == 0:
                fibo_even_sum = fibo_even_sum + fibo_sum
                #Stop if the sum exceeds tme max allowed
                if fibo_even_sum > FIBO_EVEN_SUM_MAX:
                    break

        return fibo_even_sum

def main():
    def usage():
        sys.stderr.write('Usage: %s number\n' % os.path.basename(sys.argv[0]))
        sys.exit(1)

    if len(sys.argv) != 2:
        usage()

    try:
        fib_sum= fibonacci_even_seq_sum(sys.argv[1])
    except ValueError:
        usage()
    else:
        print 'The sum of the even-valued terms is %s' % (fib_sum,)

if __name__ == '__main__':
    main()
 