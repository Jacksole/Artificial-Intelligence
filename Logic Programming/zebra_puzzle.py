'''
There are five houses.
The English man lives in the red house.
The Swede has a dog.
The Dane drinks tea.
The green house is immediately to the left of the white house.
They drink coffee in the green house.
The man who smokes Pall Mall has birds.
In the yellow house they smoke Dunhill.
In the middle house they drink milk.
The Norwegian lives in the first house.
The man who smokes Blend lives in the house next to the house with cats.
In a house next to the house where they have a horse, they smoke Dunhill.
The man who smokes Blue Master drinks beer.
The German smokes Prince.
The Norwegian lives next to the blue house.
They drink water in a house next to the house where they smoke Blend.
'''

import time

from kanren import *
from kanren.core import lall


def left(q, p, list):
    return membero((q, p), zip(list, list[1:]))


def next(q, p, list):
    return conde([left(q, p, list)], [left(p, q, list)])


houses = var()

rules_zebraproblem = lall(
    (eq, (var(), var(), var(), var(), var()), houses),

    (membero, ('Englishman', var(), var(), var(), 'red'), houses),
    (membero, ('Swede', var(), var(), 'dog', var()), houses),
    (membero, ('Dane', var(), 'tea', var(), var()), houses),
    (left, (var(), var(), var(), var(), 'green'),
        (var(), var(), var(), var(), 'white'), houses),
    (membero, (var(), var(), 'coffee', var(), 'green'), houses),
    (membero, (var(), 'Pall Mall', var(), 'birds', var()), houses),
    (membero, (var(), 'Dunhill', var(), var(), 'yellow'), houses),
    (eq, (var(), var(), (var(), var(), 'milk', var(), var()), var(), var()), houses),
    (eq, (('Norwegian', var(), var(), var(), var()), var(), var(), var(), var()), houses),
    (next, (var(), 'Blend', var(), var(), var()),
        (var(), var(), var(), 'cats', var()), houses),
    (next, (var(), 'Dunhill', var(), var(), var()),
        (var(), var(), var(), 'horse', var()), houses),
    (membero, (var(), 'Blue Master', 'beer', var(), var()), houses),
    (membero, ('German', 'Prince', var(), var(), var()), houses),
    (next, ('Norwegian', var(), var(), var(), var()),
        (var(), var(), var(), var(), 'blue'), houses),
    (next, (var(), 'Blend', var(), var(), var()),
        (var(), var(), 'water', var(), var()), houses),
    (membero, (var(), var(), var(), 'zebra', var()), houses)
)

solutions = run(0, houses, rules_zebraproblem)

output_zebra = [house for house in solutions[0] if 'zebra' in house][0][0]

print('\n' + output_zebra + ' owns zebra.')
