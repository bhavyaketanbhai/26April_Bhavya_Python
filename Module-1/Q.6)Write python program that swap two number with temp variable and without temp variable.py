# Write python program that swap two number with temp variable and
# without temp variable

# with temp variable

a=54
b=75

print("A",a)
print("B",b)

# swapping with temp

temp=a
a=b
b=temp

print("After A=",a)
print("After B=",b)

#swapping without temp

a,b=b,a

print("After A=",a)
print("After B=",b)