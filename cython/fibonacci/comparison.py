import time
from pyfibonacci import fib as pyfib
from cyfibonacci import fib, fib_int, fib_cdef, fib_cpdef

def check_time(function, argument):
    start_time = time.time()
    function(argument)
    end_time = time.time() - start_time
    print(function, end_time)


def do_test(number):
    check_time(pyfib, number)
    check_time(fib, number)
    check_time(fib_int, number)
    check_time(fib_cdef, number)
    check_time(fib_cpdef, number)

if __name__ == "__main__":
    do_test(30)