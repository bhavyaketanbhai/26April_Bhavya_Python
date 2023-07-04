import random

def random_item(lst):
    return random.choice(lst)
my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
random_fruit = random_item(my_list)
print(random_fruit)