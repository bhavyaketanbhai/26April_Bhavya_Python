# 56.Write a Python program to read a random line from a file.

import random
import linecache
filename = "myfile.txt"
with open(filename, "r") as file:
    num_lines = sum(1 for line in file)
    random_line_number = random.randint(1, num_lines)
    random_line = linecache.getline(filename, random_line_number)
    print(random_line)