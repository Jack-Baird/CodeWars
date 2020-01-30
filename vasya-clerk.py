#! python

from unittest import test

"""Vasya - Clerk - 6kyu
"""

test1 = [25, 25, 50] # Expecting: "YES"
test2 = [25, 100] # Expecting: "NO"

def tickets(people):

    till = 0
    ticket = 25

    for person in people:

        change = person - ticket
        till += ticket

        if till < change:
            return 'NO'
    
    return 'YES'

print(tickets(test1))
print(tickets(test2))