# 62.Write a Python program to returns sum of all divisors of a number

def sum_divisors(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)

n = 24
print(f"The sum of all divisors of {n} is {sum_divisors(n)}.")