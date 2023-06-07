# Write a Python program to find whether a given number is even or odd,
# print out an appropriate message to the user. 

number=int(input('Enter a number'))
remainder = number%2
if(remainder == 0):
    print("{} is an even number".format(number))
else:
    print("{} is an odd number".format(number))