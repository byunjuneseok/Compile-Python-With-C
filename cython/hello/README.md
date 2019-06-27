# Hello World

## Cython의 구조
* `hello.pyx` : Cython 코드를 포함하고 있다.
* `test.py` : `hello` 확장모듈(extension)을 호출하는 스크립트.
* `setup.py` : Cython코드를 컴파일한다.





## 스크립트 작성

### `hello.pyx`

```cython
from libc.math cimport pow

cdef double square_and_add(double x):
    return pow(x, 2.0) + x

cpdef print_result(double x):
    print("({} ^ 2) + {} = {}".format(x, x, square_and_add(x)))
    
```

* `def` : "Basically, it's python!"

* `cdef` : "Basically, it's C!"

* `cpdef` : "It's Both"

  >  *이에 대한 자세한 비교는 [Fibonacci](../fibonacci) 를 참고한다.*



### `setup.py`

```python
from distutils.core import Extension, setup
from Cython.Build import cythonize

ext = Extension(name="hello", sources=["hello.pyx"])
setup(ext_modules=cythonize(ext))

```



### `test.py`

```python
import hello

# Test!
hello.print_result(23.0)
```





## 컴파일

1. Cython 파일을 컴파일합니다.

  ```bash
  python3 setup.py build_ext --inplace
  ```



2. 임포트하여 실행합니다.

   ```Bash
   python3 test.py
   ```

