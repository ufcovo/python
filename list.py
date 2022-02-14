def dels(lst1, lst2):
    # checking if lst1 is longer than lst2
    if len(lst1) > len(lst2):
        # removing first len(lst2) number of elements from lst1
        lst1 = lst1[len(lst2):]
        # returning it
        return lst1
    # otherwise checking if lst1 is shorter than lst2
    elif len(lst1) < len(lst2):
        # taking first element of lst2, adding to a list, combining with elements of lst1
        # and then combining with rest of elements in lst2, returning combined list
        # note: + operation on two list will return a new list containing combined elements
        # for example if a=[1,2] and b=[3,4,5], a+b will return [1,2,3,4,5]
        # also, lst2[1:] will return a list with all elements of lst2 except the first element.
        return [lst2[0]] + lst1 + lst2[1:]
    # otherwise (same length) returning empty list
    else:
        return []

list1 = input ("Enter first list: ")
list2 = input ("Enter second list: ")
print (dels(list1, list2))
