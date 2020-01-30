#! python

"""Categorise New Member - 7kyu
"""

test1 = [[45, 12],[55,21],[19, -2],[104, 20]] # Expected: ['Open', 'Senior', 'Open', 'Senior'])
test2 = [[45, 12],[55,21],[19, -2],[104, 20]] # Expected: ['Open', 'Senior', 'Open', 'Senior'])

def openOrSenior(data):

    output = []

    for person in data:
        age = person[0]
        handicap = person[1]

        if int(age) >= 55 and int(handicap) > 7:
            output.append( 'Senior')
        
        else:
            output.append( 'Open')

    return output

print(f'Test 1:\n{openOrSenior(test1)}\n')
print(f'Test 2:\n{openOrSenior(test2)}\n')