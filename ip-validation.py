"""
IP Validation - 6kyu
https://www.codewars.com/kata/515decfd9dcfc23bb6000006/train/python

Write an algorithm that will identify valid IPv4 addresses in dot-decimal format.
IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

Input to the function is guaranteed to be a single string.
"""

test_data = [
    "0.0.0.0", #* Valid
    "1.2.3.4", #* Valid
    "123.45.67.89", #* Valid
    "12.34.56 .1", #! Invalid
    "1.2.3", #! Invalid
    "1.2.3.4.5", #! Invalid
    "123.456.78.90", #! Invalid
    "123.045.067.089", #! Invalid
    ""
]

def is_valid_ip(string):
    """Checks a string to determine
    if it is a valid IPv4 address.

    Args:
        string (str): Potential IPv4 address

    Returns:
        Bool: True if valid IPv4; False if not.
    """
    ip = string.split('.')
    try:
        cond0 = [[int(y) for y in x] for x in ip]
        cond1 = len(ip) == 4
        cond2 = all([0 <= int(x) <= 255 for x in ip])
        cond3 = all([(int(x) == 0 or x[0] != '0') for x in ip])

        return True if all([cond1, cond2, cond3]) else False
    except ValueError as e:
        return False

print([is_valid_ip(x) for x in test_data])