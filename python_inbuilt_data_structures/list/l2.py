
####################################################### Shallow copy #######################################################
"""once if copy of list object got created, if it contains any nested list objects, 
then if we perform any modifications on nested list object, those modifications will 
be reflected for both list objects i.e. nested list objects are shared. this type of 
copy operation is called as shallow copy or normal copy."""

"""Example: 1"""
L1 = [11, 22, 33, [111, 222, 333], 44, 55]
L2 = L1.copy() #shallow copy

print(L1) #[11, 22, 33, [111, 222, 333], 44, 55]
print(L2) #[11, 22, 33, [111, 222, 333], 44, 55]

L1[3][1] = 999

print(L1) #[11, 22, 33, [111, 999, 333], 44, 55]
print(L2) #[11, 22, 33, [111, 999, 333], 44, 55]

"""Example: 2"""
import copy
L1 = [11, 22, 33, [111, 222, 333], 44, 55]
L2 = copy.copy(L1) #shallow copy

print(L1) #[11, 22, 33, [111, 222, 333], 44, 55]
print(L2) #[11, 22, 33, [111, 222, 333], 44, 55]

L1[3][1] = 777

print(L1) #[11, 22, 33, [111, 777, 333], 44, 55]
print(L2) #[11, 22, 33, [111, 777, 333], 44, 55]


####################################################### Deep copy #######################################################
"""once if copy of list object got created, if it contains any nested list objects, 
then if we perform any modifications on nested list object, those modifications will 
be reflected for only one  list objects i.e. nested list objects are not shared. this 
type of copy operation is called as deep copy.
"""
"""Example:"""
import copy
L1 = [11, 22, 33, [111, 222, 333], 44, 55]
L2 = copy.deepcopy(L1) #deep copy

print(L1) #[11, 22, 33, [111, 222, 333], 44, 55]
print(L2) #[11, 22, 33, [111, 222, 333], 44, 55]

L1[3][1] = 666

print(L1) #[11, 22, 33, [111, 666, 333], 44, 55]
print(L2) #[11, 22, 33, [111, 222, 333], 44, 55]