newlist = ['list1', 'list2', 'list3', 'list4', 'list5']

#print(newlist)
#print(len(newlist))

def chop(lst):
    del lst[0]
    del lst[(len(lst)-1)]
    return None

def middle(lst):
    lst = list()
    for item in lst:
        if item == lst[0] or lst[(len(lst)-1)]:
            continue
        lst.append(item)
    return lst

chop(newlist)
print(newlist)
