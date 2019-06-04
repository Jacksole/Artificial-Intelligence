'''
Checking for prime numbers
'''
# Requried Modules
import itertools as it

from sympy.ntheory.generate import isprime, prime

from kanren import isvar, membero, run
from kanren.core import condeseq, eq, fail, goaleval, success, var


def prime_check(x):
    if isvar(x):
        return condeseq([(eq, x, p)] for p in map(prime, it.count(1)))
    else:
        return success if isprime(x) else fail


x = var()
print((set(run(0, x, (membero, x, (12, 14, 15, 19, 20, 21, 22, 23, 29, 30, 41, 44, 52, 62, 65, 85)),
               (prime_check, x)))))
print((run(10, x, prime_check(x))))
