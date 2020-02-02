#! python

"""Who Likes it? - 6kyu
"""

test_lists = [
    ['Peter'],
    ['Jacob', 'Alex'],
    ['Max', 'John', 'Mark'],
    ['Alex', 'Jacob', 'Mark', 'Max']
]

def likes(names):
    people = len(names)

    if people == 0:
        return 'no one likes this'
    
    elif people == 1:
        return f'{names[0]} likes this'

    elif people == 2:
        return f'{names[0]} and {names[1]} like this'

    elif people == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'

    else:
        return f'{names[0]}, {names[1]} and {int(people - 2)} others like this'

print([likes(x) for x in test_lists])