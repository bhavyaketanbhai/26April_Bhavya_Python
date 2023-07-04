# 43.Write a Python program to create and display all combinations of letters,
# selecting each letter from a different key in a dictionary.

import itertools

my_dict = {'a': 'abc', 'b': 'def', 'c': 'ghi'}

combinations = list(itertools.product(*[my_dict[key] for key in my_dict]))

for combination in combinations:
    print(''.join(combination))