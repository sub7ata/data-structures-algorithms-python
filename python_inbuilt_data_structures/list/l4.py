################################## Common functions on list ####################################
L = [10, 20, 30, 40, 50]
print(len(L))			
print(max(L))
print(min(L))
print(sorted(L))
print(sorted(L,reverse=True))
print(sum(L))


################################### List specific methods #####################################

"""append(object): it is used to add an object into list at the ending."""
L = [10, 20, 30, 40]
print(L) #[10, 20, 30, 40]
L.append(50)
print(L) #[10, 20, 30, 40, 50]

"""insert(index,object): it is used to add an object into list at the given index value"""
L = [10, 20, 30, 40]
print(L) #[10, 20, 30, 40]
L.insert(0,999)
print(L) #[999, 10, 20, 30, 40]

"""remove(object): it will remove the given object from the list"""
L = [10, 20, 30, 40]
print(L) #[10, 20, 30, 40]
L.remove(20)
print(L) #[10, 30, 40]

"""pop(): it will remove the element located at last location"""
L = [10, 20, 30, 40]
print(L) #[10, 20, 30, 40]
L.pop()
print(L) #[10, 20, 30]

"""pop(index): it will remove the element located at given location"""
L = [10, 20, 30, 40]
print(L) #[10, 20, 30, 40]
L.pop(0)
print(L) #[20, 30, 40]

"""clear(): it will remove all the elements from a list"""
L = [10, 20, 30, 40]
print(L) #[10, 20, 30, 40]
L.clear()
print(L) #[]


"""index(object): it returns location of the given object"""
L = [10, 20, 30, 40, 10, 20, 20, 10, 20]
print(L) 
print(L.index(30)) #2
# print(L.index(70)) #Error 

"""count(object): it returns number of occurrences of the given object"""
L = [10, 20, 30, 40, 10, 20, 20, 10, 20]
print(L) 
print(L.count(10)) #3
print(L.count(20)) #4 

"""reverse(): it reverse the given list object"""
L = [10, 30, 20, 50, 40]
print(L) #[10, 30, 20, 50, 40]
L.reverse()
print(L) #[40, 50, 20, 30, 10]

"""sort(): it sorts the given list in asc order"""
L = [10, 30, 20, 50, 40]
print(L) #[10, 30, 20, 50, 40]
L.sort()
print(L) #[10, 20, 30, 40, 50]

"""sort(reverse=True): it sorts the given list in desc order"""
L = [10, 30, 20, 50, 40]
print(L) #[10, 30, 20, 50, 40]
L.sort(reverse=True)
print(L) #[50, 40, 30, 20, 10]