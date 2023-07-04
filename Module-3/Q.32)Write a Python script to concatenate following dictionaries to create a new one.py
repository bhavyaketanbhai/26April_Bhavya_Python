# 32.Write a Python script to concatenate following dictionaries to create a
# new one

dict1 = {'apple': 5, 'banana': 2, 'cherry': 4}
dict2 = {'date': 3, 'elderberry': 1}
dict3 = {'fig': 6, 'grape': 2}

new_dict = {**dict1, **dict2, **dict3}

print("Concatenated dictionary:", new_dict)