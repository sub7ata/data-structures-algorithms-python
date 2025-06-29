"""Difference of Sets"""
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
difference_set = set1.difference(set2)
print("Difference (set1 - set2):", difference_set)

symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference_set)


"""Add a list of Elements to a Set"""
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

sample_set.update(sample_list)
print(sample_set)


"""Find Common Elements in Two Lists"""
list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

set_list1 = set(list1)
set_list2 = set(list2)

common_elements = set_list1.intersection(set_list2)
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Common elements using sets: {common_elements}")


"""Set Symmetric Difference Update"""
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.symmetric_difference_update(set2)
print(set1)

