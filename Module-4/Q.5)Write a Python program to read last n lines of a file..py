# 5.Write a Python program to read last n lines of a file.

with open('filename.txt', 'r') as file:
    n = 5
    lines = file.readlines()
    last_n_lines = lines[-n:]
    for line in last_n_lines:
        print(line)