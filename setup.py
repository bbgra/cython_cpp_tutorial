#  Copyright (c) 2020 Andreas Buchberger
#
#  This file is licensed under the MIT license.
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY  WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE  SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

from setuptools import setup, find_packages, Extension
import sys
from Cython.Build import cythonize

# Define general Cython compiler cython_directives
# Essentially, we turn off any check -> make sure the c/++ code works!
cython_directives = {'boundscheck': False,
                     'wraparound': False,
                     'cdivision': True,
                     'initializedcheck': False,
                     }

# Define the C++/Cython package
WIN_COMPILER_ARGS = ["/O2"]
WIN_LINK_ARGS = None
COMPILER_ARGS = ["-O3"]
LINK_ARGS = None

cython_name = 'cython_cpp_tutorial.cython_function.function'
cython_sources = ['cython_cpp_tutorial/cython_function/function.pyx']
cython_include = ['cython_cpp_tutorial/cython_function/']

if sys.platform.startswith("win"):
    function_cython = Extension(name=cython_name,
                                sources=cython_sources,
                                include_dirs=cython_include,
                                language='c++',
                                extra_compile_args=WIN_COMPILER_ARGS,
                                extra_link_args=WIN_LINK_ARGS)
else:
    function_cython = Extension(name=cython_name,
                                sources=cython_sources,
                                include_dirs=cython_include,
                                language='c++',
                                extra_compile_args=COMPILER_ARGS,
                                extra_link_args=LINK_ARGS)

setup(
    name='cython_cpp_tutorial',
    version='0.1dev0',
    description='A tutorial package to wrap C/C++ code.',
    long_description=None,
    author='Andreas Buchberger',
    author_email='andreas.buchberger@chalmers.se',
    url=None,
    license='MIT',
    install_requires=['numpy'],
    packages=find_packages(exclude=['bin', 'build', 'matlab', 'docs', 'test']),
    ext_modules=cythonize([function_cython],
                          compiler_directives=cython_directives),
)
