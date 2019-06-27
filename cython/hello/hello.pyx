from libc.math cimport pow

cdef double square_and_add(double x):
    # Cython에서만 호출이 가능합니다.
    return pow(x, 2.0) + x

cpdef print_result(double x):
    # Cython, Python 에서 호출이 가능합니다.
    print("({} ^ 2) + {} = {}".format(x, x, square_and_add(x)))
