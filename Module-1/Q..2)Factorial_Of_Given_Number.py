# 2)Write a Python program to get the Factorial number of given number.

number = int(input("Enter an Number:"))
fact = 1
y=1
while y<=number:
    fact=fact*y
    y=y+1
print("The Factorial of ",number,"is",fact)