# 44.Write a Python program to find the highest 3 values in a dictionary

my_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 30, 'e': 25}

highest_values = sorted(my_dict.values(), reverse=True)[:3]

print(highest_values)