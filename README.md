# Implementation in Python - Partitions of totally positive integers in real quadratic fields
This is the implementation of the algorithm described in my Bachelor's thesis: Partitions of totally positive elements in real quadratic fields for the year 2022/2023.

The algorithm and theory behind it is described in the thesis above. The program is written in Python 3.8.6 with the Python Math Library included. Newer versions of Python should work also.

## Documentation
For the documentation, please see the PDF version of the thesis mentioned.

## Usage:
### Input:
After running the program, the user is asked for three inputs:
  1. Input D > 0 for quadratic field Q(sqrt(D))
    - D is an integer, that must be square-free
  2. Input the integer: 'a + b.omega_D' in the form: 'a b'
    - if 'a + b.omega_D' is not totally positive in Q(sqrt(D)), then the output is zero
  3. Do you want to print all the partitions? Input Y/N:
    - this prints all the partitions in the form [(a,b), (c,d), ...]
  
### Output:
The output is the number of partitions (with each partition printed, if the user wants) of totally positive integer 'a + b.omega_D'. If 'a + b*omega_D' is not totally positive in Q(sqrt(D)), then the output is zero. Also, if D is not a square free integer, the program will give an arror.
