def common_member(lst1, lst2):
    for item in lst1:
        if item in lst2:
            return True
    return False
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]
if common_member(list1, list2):
    print("The lists have at least one common member")
else:
    print("The lists do not have any common members")