# 11.Write a Python program to write a list to a file.

my_list = ["apple", "orange", "banana"]

with open("filename.txt", "w") as file:
    for item in my_list:
        file.write(item + "\n")