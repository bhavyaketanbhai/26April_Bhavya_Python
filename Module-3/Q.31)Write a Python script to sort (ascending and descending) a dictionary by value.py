# # 31 Write a Python script to sort (ascending and descending) a dictionary by
# value


my_dict = {'apple': 5, 'banana': 2, 'cherry': 4, 'date': 3, 'elderberry': 1}

sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Dictionary sorted by value in ascending order:", sorted_dict)
print("Dictionary sorted by value in descending order:", sorted_dict_desc)
