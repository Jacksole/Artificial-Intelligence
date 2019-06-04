'''
finding the unknown values by using logic programming in a very effective way
https://www.tutorialspoint.com/artificial_intelligence_with_python/artificial_intelligence_with_python_logic_programming.htm
'''
from kanren import fact, run, var
from kanren.assoccomm import associative, commutative
from kanren.assoccomm import eq_assoccomm as eq

add = 'add'
mul = 'mul'

fact(commutative, mul)
fact(commutative, add)
fact(associative, mul)
fact(associative, add)

a, b = var('a'), var('b')

original_pattern = (mul, (add, 5, a), b)

exp1 = (mul, 2, (add, 3, 1))
exp2 = (add, 5, (mul, 8, 1))

print(run(0, (a, b), eq(original_pattern, exp1)))
print(run(0, (a, b), eq(original_pattern, exp2)))
