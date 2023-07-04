def count_strings(strings):
    count = 0
    for string in strings:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count
my_list = ['abca', 'xyz', 'aa', 'bbb', 'xyx']
count = count_strings(my_list)
print(count)