# 45.Write a Python program to combine values in python list of dictionaries.

my_list = [{'a': 10, 'b': 5}, {'a': 20, 'b': 15}, {'a': 30, 'b': 25}]

combined_values = {}

for item in my_list:
    for key, value in item.items():
        if key in combined_values:
            combined_values[key] += value
        else:
            combined_values[key] = value

print(combined_values)