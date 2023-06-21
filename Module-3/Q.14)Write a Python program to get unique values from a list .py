# 14.Write a Python program to get unique values from a list 

list=[1,4,4,6,4,6,3,5,3,6]
unique_list=[]
for a in list:
    if a not in unique_list:
        unique_list.append(a)
print(unique_list)