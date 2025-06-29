"""Replace list’s item with new value if found"""
lst = [10,20,30,40,50,20,30,40,20]
p = lst.index(20)
lst[p] = 9999
print(lst)


"""Reverse of a list"""
lst = [10,20,30,40,50,20,30,40,20]
lst1 = sorted(lst, reverse=True)
print(lst1)

lst.sort(reverse=True)
print(lst)


"""Get the difference between the two Lists"""
list1 = ['Scott', 'Eric', 'Kelly', 'Emma', 'Smith']
list2 = ['Scott', 'Eric', 'Kelly']

set1 = set(list1)
set2 = set(list2)

list3 = list(set1.symmetric_difference(set2))
print(list3)


"""How to efficiently compare two unordered lists"""
from collections import Counter
one = [33, 22, 11, 44, 55]
two = [22, 11, 44, 55, 33]
print("is two list are b equal", Counter(one) == Counter(two))


"""How to check if all elements in a list are unique"""
def isUnique(item):
    tempSet = set()
    return not any(i in tempSet or tempSet.add(i) for i in item)

listOne = [123, 345, 456, 23, 567]
print("All List elemtnts are Unique ", isUnique(listOne))

listTwo = [123, 345, 567, 23, 567]
print("All List elemtnts are Unique ", isUnique(listTwo))