#! python

"""Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string
The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
"""

tests = ['abcde', 'abcdea', 'indivisbility', 'quagmire', 'bonobo', 'house', 'seafront', 'pisces', 'apple', 'banana']

def duplicate_count(text):
    text = text.lower()
    duplicate_letters = []

    [duplicate_letters.append(x) for x in text if (text.count(x) > 1) & (x not in duplicate_letters)]

    return len(duplicate_letters)

print([duplicate_count(x) for x in tests])