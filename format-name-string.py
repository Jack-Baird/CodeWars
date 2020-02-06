#! python

"""Format a string of names like 'Bart, Lisa & Maggie'. 6kyu
"""

list1 = [{'name':'Bart'}, {'name':'Lisa'}, {'name':'Maggie'}, {'name':'Homer'}, {'name':'Marge'}]
list2 = [{'name':'Bart'}, {'name':'Lisa'}, {'name':'Maggie'}]
list3 = [{'name':'Bart'}, {'name':'Lisa'}]
list4 = [{'name':'Bart'}]
list5 = []


def namelist(names):
    num_names = len(names)
    
    if num_names == 0:
        return []
    
    elif num_names == 1:
        return names[0]['name']

    elif num_names == 2:
        return f"{names[0]['name']} & {names[1]['name']}"
    
    else:
        first = str([names[x]['name'] + ', ' for x in range(num_names - 1)])
        last = f"{names[num_names - 2]['name']} & {names[num_names - 1]['name']}"
        return first + last

print([namelist(x) for x in [list1, list2, list3, list4, list5]])