# 6.Write a Python program to read a file line by line and store it into a list

lines = []
with open('filename.txt', 'r') as file:
    for line in file:
        lines.append(line.strip())
print(lines)