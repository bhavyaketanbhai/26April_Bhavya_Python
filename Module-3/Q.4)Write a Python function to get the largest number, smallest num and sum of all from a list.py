def get_list_stats(numbers):
    largest = max(numbers)
    smallest = min(numbers)
    total = sum(numbers)
    return largest, smallest, total
my_list = [1, 2, 3, 4, 5]
largest, smallest, total = get_list_stats(my_list)
print("Largest number:", largest)
print("Smallest number:", smallest)
print("Sum of all numbers:", total)