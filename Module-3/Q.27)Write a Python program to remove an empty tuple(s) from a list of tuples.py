my_list = [(1, 2), (), (3, 4), (), (5,), (), (), (6, 7, 8)]
new_list = [tup for tup in my_list if tup]

print(new_list)