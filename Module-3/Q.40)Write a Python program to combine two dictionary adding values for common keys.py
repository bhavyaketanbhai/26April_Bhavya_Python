# 40.Write a Python program to combine two dictionary adding values for
# common keys

dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 300, 'b': 200, 'd': 400}

for key in dict2:
    if key in dict1:
        dict1[key] += dict2[key]
    else:
        dict1[key] = dict2[key]

print(dict1)