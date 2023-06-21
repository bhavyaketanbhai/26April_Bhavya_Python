# Write a Python program to test whether a passed letter is a vowel or
# not. 
x=input("Enter any Alphabet:")
x=x.lower()
if(x=='a' or x=='e' or x=='i' or x=='o' or x=='u'):
    print("It Is Vowel.")
else:
    print("It is consonant.")