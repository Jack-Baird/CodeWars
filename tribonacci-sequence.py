#! python

"""Tribonacci Sequence - 6kyu # The Tribonacci Sequence is modelled on the Fibonacci Sequence,
however it uses the last three (not two) numbers to generate the next in the sequence.
"""

signatures = {
    'a':([1, 1, 1], 10),
    'b':([0, 0, 1], 10),
    'c':([0, 1, 1], 10),
    'd':([1, 0, 0], 10),
    'e':([0, 0, 0], 10),
    'f':([1, 2, 3], 10),
    'g':([3, 2, 1], 10),
    'h':([1, 1, 1], 1),
    'i':([300, 200, 100], 0),
    'j':([0.5, 0.5, 0.5], 30)
}

def tribonacci(signature, n):
    """Calculates the Tribonacci sequence generated
    by the three-digit signature and returns the
    first n elements - signature included.
    
    Arguments:
        signature {list} -- List containing 3-digit initial sequence.
        n {int} -- Non-negative integer.
    """

    if n <= 0:
        return []

    sequence = signature

    i = 0
    while i < n - 3:
        sequence.append(sum(sequence[-3:]))
        i += 1

    return sequence[:n]

for key in signatures:
    print(f'Item {key} - Sig: {signatures[key][0]} - N: {signatures[key][1]} - Seq: {tribonacci(signatures[key][0], signatures[key][1])}')