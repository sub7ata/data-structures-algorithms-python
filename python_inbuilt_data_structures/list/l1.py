##################################################### Accessing list objects #####################################################
L = [10, 20, 30, 40]
print(L)
print(L[0:len(L)])
print(L[::])

index = 0
while index<len(L):
	print(L[index])
	index = index + 1

for item in L:
	print(item)

####################################################### Nested list objects #######################################################
nested = [[1, 2], [3, 4]]
for i, sub in enumerate(nested):
    for j, val in enumerate(sub):
        print(f"nested[{i}][{j}] = {val}")


import itertools
nested = [100, 200, [111, 222, 333], 300, 400, 500]
flat = list(itertools.chain.from_iterable(
    item if isinstance(item, list) else [item] for item in nested
))
print(flat)

####################################################### List aliasing #######################################################
"""Example: 1"""
L1 = [1, 2, 3, 4, 5]
L2 = L1
print(L1 is L2)

"""Example: 2"""
L1 = [1, 2, 3, 4, 5]
L2 = L1
print(L1)
print(L2)

L1[2] = 999
print(L1)
print(L2)


####################################################### List cloning #######################################################

"""Example: 1"""
L1 = [1, 2, 3, 4, 5]
L2 = L1.copy()
print(L1)
print(L2)
print(L1 is L2)

"""Example: 2"""
L1 = [1, 2, 3, 4, 5]
L2 = L1.copy()
print(L1)
print(L2)

L1[2] = 888
print(L1) #[1, 2, 888, 4, 5]
print(L2) #[1, 2, 3, 4, 5]


"""Example1: Nested list"""
L1 = [11, 22, 33, [111, 222, 333], 44, 55]
L2 = L1.copy()

print(L1) #[11, 22, 33, [111, 222, 333], 44, 55]
print(L2) #[11, 22, 33, [111, 222, 333], 44, 55]

L1[1] = 888

print(L1) #[11, 888, 33, [111, 222, 333], 44, 55]
print(L2) #[11, 22, 33, [111, 222, 333], 44, 55]

"""Example2: Nested list"""
L1 = [11, 22, 33, [111, 222, 333], 44, 55]
L2 = L1.copy()

print(L1) #[11, 22, 33, [111, 222, 333], 44, 55]
print(L2) #[11, 22, 33, [111, 222, 333], 44, 55]

L1[3][1] = 999

print(L1) #[11, 22, 33, [111, 999, 333], 44, 55]
print(L2) #[11, 22, 33, [111, 999, 333], 44, 55]