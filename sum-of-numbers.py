#! python

"""Beginner Series #3 Sum of Numbers - 7kyu
"""

def get_sum(a, b):
    c = int(min(a, b))
    d = int(max(a, b))

    ints = []

    if c == d:
        return c

    else:
        for i in range(c, d + 1):
            ints.append(i)
            
        return sum(ints)

print(get_sum(84, 71))
print(get_sum(0, 1))
print(get_sum(0, -1))
print(get_sum(-1, 2))