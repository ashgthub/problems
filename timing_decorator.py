import time

"""
A decorator that calculates the time taken to execute 
the wrapped function.
"""
def calculate_timing(func):
    def wrapper(*arg, **kwargs):
    	#start the timer
        start_time = time.time()
        result = func(*arg, **kwargs)
        #stop the timer
        end_time = time.time()
        print '%s took %0.5f ms' % (func.func_name, (end_time-start_time)*1000.0)
        return result
    return wrapper