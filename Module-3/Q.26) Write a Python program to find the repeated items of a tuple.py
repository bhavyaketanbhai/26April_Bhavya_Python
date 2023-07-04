my_tuple = (1, 2, 3, 2, 4, 5, 3, 6, 7, 3)
repeated_items = []

for item in my_tuple:
    if my_tuple.count(item) > 1 and item not in repeated_items:
        repeated_items.append(item)

print(repeated_items)