
#====================================================== List Comprehension ==========================================================#
"""syntax1: [expr for i in sequence]
syntax2: [expr for i in sequence if condition]"""

"""Example1: increment each element present in a list"""
OL = [1, 2, 3, 4, 5]
NL = [i+1 for i in OL]
print(OL) #[1, 2, 3, 4, 5]
print(NL) #[2, 3, 4, 5, 6]

"""Example2: find factorial of each element present in a list"""
import math
OL = [1, 2, 3, 4, 5]
NL = [math.factorial(i) for i in OL]
print(OL) #[1, 2, 3, 4, 5]
print(NL) #[1, 2, 6, 24, 120]

"""Example3: convert every name present in list into upper case"""
OL = ["prakash","raju","ram","somu"]
NL = [i.upper() for i in OL]
print(OL) #[prakash, raju, ram, somu]
print(NL) #[PRAKASH, RAJU, RAM, SOMU]

"""Example4: extract even numbers from a list"""
OL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
NL = [i for i in OL if i%2==0]
print(OL) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(NL) #[2, 4, 6, 8, 10]
