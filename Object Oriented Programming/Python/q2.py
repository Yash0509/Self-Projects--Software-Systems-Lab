import argparse
import sys
import functools
import operator
import matplotlib.pyplot as plt
# This python module can be used for getting the input provided by user
  
def get_primes(num):
   # Should take an integer as input and reutrn a list of primes less than or equal to the given input
    primes = functools.reduce(lambda r, x: r - set(range(x**2, num, x)) if x in r else r, range(2, int(num**1) + 1), set(range(2,num)))
    s = list(primes)
    print(s)
    
    # print('matplotlib: {}'.format(matplotlib.__version__))
    plt.plot(s, s)
    plt.show()

num = 0
if __name__ == '__main__':
    # Edit this part of the code in order to pass the argument to get_primes() function
    # num is the argument you got from command line using argparse module
    num = int(sys.argv[1])
    get_primes(num)