# 4.Write a Python program to read first n lines of a file.

with open('filename.txt', 'r') as file:
    n = 5
    for i in range(n):
        line = file.readline()
        print(line)