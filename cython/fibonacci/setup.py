from distutils.core import Extension, setup
from Cython.Build import cythonize

ext = Extension(name="cyfibonacci", sources=["cyfibonacci.pyx"])
setup(ext_modules=cythonize(ext))
