# Write a Python function that takes a list of words and returns the length
# of the longest one

def count_word_lenght(my_list):
    counter=0
    for item in my_list:
        if len(item) >= counter:
           counter=len(item)
           return counter
        
        temp_list=["hello","bhavya"]
        print("longest word count is %d"%count_word_lenght(temp_list))