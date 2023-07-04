# 50.Write a Python function that checks whether a passed string is
# palindrome or not

def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
    result = is_palindrome("racecar")
    print(result)