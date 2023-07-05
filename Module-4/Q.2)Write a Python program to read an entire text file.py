# 2.Write a Python program to read an entire text file.

with open('filename.txt', 'r') as file:
    data = file.read()
    print(data)