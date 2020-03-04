# Tutorial to call C/C++ code in  Python
This tutorial assumes that you have a working Python environment up and running.

## Installing Cython
Use your Python package manager of choice (e.g., Anaconda/Conda, pip, ...) to install the package `Cython`.

## Installing a C/C++ compiler
### Windows
Building C/C++ code to work together with Python needs to be compiled with exactly the same compiler that was used to build the Python binaries. For Python 3.6, it is Visual Studio 2015 Community Edition and can be downloaded [here](https://visualstudio.microsoft.com/downloads/).

Note that if you do not use the correct version of Visual Studio, you will encounter very strange and cryptic compilation errors. Also, when installing, make sure to actually install the C++ part for Visual Studio - it is not selected by default!

## An example
Lets assume we want to multiply an one-dimensional numpy-array with a scalar by calling a C++ function.
First, we write the C++ function with a corresponding header file. This can be found in `./cython_cpp_tutorial/cython_function/function_cpp.cpp` and `./cython_cpp_tutorial/cython_function/function_cpp.cpp`.

We then need to write a Cython function as a wrapper for the C++ function with a corresponding header file, found in `./cython_cpp_tutorial/cython_function/function.pyx` and `./cython_cpp_tutorial/cython_function/function.pyd`.

Finally, we write a Python function, wrapping the cython function (sometimes not necessary as in this example, but it is convenient to use for defining extra functionality that has nothing to do with Cython), found in `./cython_cpp_tutorial/python_function.py`.

Note that all directories contain an `__init__.py` file such that everything can be loaded as modules.

In `setup.py` we define the build chain. Note that this will install a package called cython_cpp_tutorial.

### Installing the example
Navigate to the folder and run `python setup.py develop` to build and install the package.

### Try the example
Try running `./bin/example.py`.
