def filter_list(l):
    list_=[]
    for i in l:
        if isinstance(i, int):
            list_.append(i)
    return list_
    'return a new list with the strings filtered out'