#! python

"""You're A Square! - 7kyu
"""

tests = [-1, 0, 3, 4, 25, 26]

def is_square(n):
    """Determines if n is square. Returns a Boolean.
    
    Arguments:
        n {int} -- input integer
    """
    if n >= 0 and n ** 0.5 == int(n ** 0.5):
      return True
    else:
      return False

for x in tests:
    print(is_square(x))