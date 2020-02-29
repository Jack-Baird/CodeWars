#! python

"""In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
"""

tests = ('1 2 3 4 5', '1 2 -3 4 5', '1 9 3 4 -5', '4 5 29 54 4 0 -214 542 -64 1 -3 6 -6')

def high_and_low(numbers):
    numbers = numbers.split()
    numbers = list(map(int, numbers))

    return f'{max(numbers)} {min(numbers)}'

print([high_and_low(x) for x in tests])