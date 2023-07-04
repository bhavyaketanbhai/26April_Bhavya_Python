# 37.Write a Python program to check multiple keys exists in a dictionary

my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

keys_to_check = ["key1", "key4", "key3"]

for key in keys_to_check:
    if key in my_dict:
        print(key, "exists in the dictionary")
    else:
        print(key, "does not exist in the dictionary")