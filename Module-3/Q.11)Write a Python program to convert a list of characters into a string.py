def unique_list(lst):
    return list(set(lst))
my_list = [1, 2, 3, 3, 4, 4, 5]
new_list = unique_list(my_list)
print(new_list)