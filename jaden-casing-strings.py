#! python

"""Jaden Casing Strings - 7kyu
"""

quote = "How can mirrors be real if our eyes aren't real"

def to_jaden_case(string):
    word_list = string.split()

    for x in range(len(word_list)):
        word_list[x] = word_list[x].capitalize()

    return ' '.join(word_list)

print(to_jaden_case(quote))