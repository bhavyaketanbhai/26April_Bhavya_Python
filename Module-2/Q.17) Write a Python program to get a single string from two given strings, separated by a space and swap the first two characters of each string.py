#  Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string

v2,v1="abcd","rstu"
temp=v2
v2=v1[0:2]+v2[2:]
v1=temp[0:2]+v1[2:]
print(v2+' '+v1)

# print(v1)

