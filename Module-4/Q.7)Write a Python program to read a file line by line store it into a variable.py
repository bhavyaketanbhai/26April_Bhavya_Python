# 7.Write a Python program to read a file line by line store it into a variable.

content = ""
with open("filename.txt", "r") as file:
    for line in file:
        content += line
print(content)