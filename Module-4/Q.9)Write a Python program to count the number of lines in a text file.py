# 9.Write a Python program to count the number of lines in a text file.

count = 0
with open("filename.txt", "r") as file:
    for line in file:
        count += 1
print("Number of lines:", count)