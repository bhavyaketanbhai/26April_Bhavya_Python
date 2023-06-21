# 7.Write a Python program to remove duplicates from a list

data=[1,2,3,3,5,4,6,3,4,3,2,7,4]

mydata=[]

for item in data:
    if item not in mydata:
        mydata.append(item)
print(mydata)