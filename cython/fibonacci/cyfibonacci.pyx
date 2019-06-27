def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

def fib_int(int n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

def fib_cdef(int n):
    return fib_in_c(n)

cdef int fib_in_c(int n):
    if n < 2:
        return n
    return fib_in_c(n-2) + fib_in_c(n-1)

cpdef fib_cpdef(int n):
    if n < 2:
        return n
    return fib_cpdef(n-2) + fib_cpdef(n-1)
    