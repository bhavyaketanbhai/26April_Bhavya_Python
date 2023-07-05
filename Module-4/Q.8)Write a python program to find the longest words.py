# 8.Write a python program to find the longest words.

string = "The quick brown fox jumps over the lazy dog"
words = string.split()
max_length = len(max(words, key=len))
longest_words = [word for word in words if len(word) == max_length]
print(longest_words)