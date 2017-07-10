import operator

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

def solution_asc(dic):
    dict_sort = sorted(dic.items(),key = operator.itemgetter(0),reverse = False)
    return dict_sort

print solution_asc(d)


def solution_desc(dic):
    dict_sort = sorted(dic.items(),key = operator.itemgetter(0),reverse = True)
    return dict_sort

print solution_desc(d)
