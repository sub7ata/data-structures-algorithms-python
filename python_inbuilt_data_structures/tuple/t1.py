"""Function Returning Tuple"""
def get_min_max(numbers):
    if not numbers:
        return (None, None)
    
    min_val = min(numbers)
    max_val = max(numbers)
    return (min_val, max_val)

my_numbers = [10, 5, 20, 2, 15]
min_max_values = get_min_max(my_numbers)
print(f"Original numbers: {my_numbers}")
print(f"Minimum and maximum values: {min_max_values}")


"""Removing Duplicates from Tuple"""
my_tuple = (1, 2, 2, 3, 4, 4, 5)
print(f"Original tuple with duplicates: {my_tuple}")
unique_elements_set = set(my_tuple)
unique_tuple = tuple(unique_elements_set)
print(f"Tuple with unique elements: {unique_tuple}")

from collections import OrderedDict
my_tuple = (1, 2, 2, 3, 4, 4, 5)
print(f"Original tuple with duplicates: {my_tuple}")
unique_ordered_tuple = tuple(OrderedDict.fromkeys(my_tuple))
print(f"Tuple with unique elements (order preserved): {unique_ordered_tuple}")


"""Sort a tuple of tuples by 2nd item"""
tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
print(f"Original tuple: {tuple1}")

list1 = list(tuple1)
sorted_list = sorted(list1, key=lambda item: item[1])
sorted_tuple = tuple(sorted_list)
print(f"Sorted tuple by 2nd item: {sorted_tuple}")