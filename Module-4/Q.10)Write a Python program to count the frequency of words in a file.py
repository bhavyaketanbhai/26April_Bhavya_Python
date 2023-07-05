# 10.Write a Python program to count the frequency of words in a file.

from collections import Counter

with open("filename.txt", "r") as file:
    words = file.read().split()
    word_count = Counter(words)

print(word_count)