# 48.Write a Python function to check whether a number is in a given range

def in_range(num, start, end):
    if num >= start and num <= end:
        return True
    else:
        return False
    result = in_range(5, 1, 10)
    print(result)