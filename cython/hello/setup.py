from distutils.core import Extension, setup
from Cython.Build import cythonize

ext = Extension(name="hello", sources=["hello.pyx"])
setup(ext_modules=cythonize(ext))
