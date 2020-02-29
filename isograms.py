#! python

"""Determines if a given string is an isogram (a word that has no repeating letters, consecutive or non-consecutive) ignoring case.
"""

tests = ['Dermatoglyphics', 'isogram', 'aba', 'moOse', 'isIsogram', '']

def is_isogram(string):
    string = list(string.lower())
    duplicates = False
    for letter in string:
        if string.count(letter) > 1:
            duplicates = True
    return True if not duplicates else False


print([is_isogram(x) for x in tests])
#print(is_isogram(tests[0]))