# 47.Write a Python function to calculate the factorial of a number (a
# nonnegative integer)

def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)
    result = factorial(5)
    print(result)