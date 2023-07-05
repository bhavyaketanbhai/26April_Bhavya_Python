# 12.Write a Python program to copy the contents of a file to another file.

with open("source_file.txt", "r") as source_file:
    with open("destination_file.txt", "w") as destination_file:
        destination_file.write(source_file.read())