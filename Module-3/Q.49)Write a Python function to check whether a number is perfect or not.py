# 49.Write a Python function to check whether a number is perfect or not.

def is_perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return True
    else:
        return False
    result = is_perfect(28)
    print(result)