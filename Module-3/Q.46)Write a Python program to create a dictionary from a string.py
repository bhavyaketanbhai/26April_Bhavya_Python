# 46.Write a Python program to create a dictionary from a string.

my_string = 'apple=3,banana=5,orange=2'

my_dict = {}

for item in my_string.split(','):
    key, value = item.split('=')
    my_dict[key] = int(value)

print(my_dict)