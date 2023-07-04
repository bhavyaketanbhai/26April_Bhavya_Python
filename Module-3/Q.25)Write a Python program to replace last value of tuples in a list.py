my_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
new_list = []

for tup in my_list:
    new_tup = tup[:-1] + (100,)
    new_list.append(new_tup)

print(new_list)