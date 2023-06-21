a=int(input("Enter Number-1 :"))
b=int(input("Enter Number-2 :"))
c=int(input("Enter Number-3 :"))
if a==b or b==c or c==a:
    print("Sum is 0 because values are both same.")
else:
    print("sum is",a+b+c)