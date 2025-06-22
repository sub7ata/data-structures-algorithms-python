"""Creation of string objects  in python"""
'''
1. single quotes
2. double quotes
3. triple single quotes
4. triple double quotes
5. input() function
6. str() type casting function
7. eval() function
'''

"""Example: 1"""
obj = input("Enter any object: ")
print(obj)
print(type(obj))

"""Example: 2"""
obj1= 222
obj2= str(obj1)
print(obj1, type(obj1))
print(obj2, type(obj2))

"""Example: 3"""
obj = eval(input("Enter any object: "))
print(obj, type(obj))


"""Accessing string objects"""
'''
1. directly
2. index concept
3. slice operator
4. while loop
5. for each loop
'''

"""Example: 1"""
s = "ijklmnop"
print(s, type(s))
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[5])
print(s[6])
print(s[7])


"""Example: 2"""
s = "wxyz"

index = 0
while index < len(s):
    print(f'index: {index} character: {s[index]}')
    index += 1


"""Example: 3"""
s = "wxyz"

index = -1
while index >= - len(s):
    print(f'index: {index} character: {s[index]}')
    index -= 1

"""for each loop"""
"""Example: """
s = "incident"

print(s)
for i in s:
    print(i)

"""Slice Operator"""
'''
version1: s[startIndex: endIndex] ---------------> startIndex to endIndex -1
version2: s[startIndex: endIndex: stepValue] ----> startIndex to stepValue -1 with step
'''

"""Example: 1"""
s = "abcdefghijklmnopqrstuvwxyz"
print(s)
print(s[0:26])
print(s[0:len(s)])
print(s[5:8])

"""Example: 2"""
s = "abcdefg"
print(s)
print(s[-7:-4])
print(s[-1:-4])

"""Example: 3"""
s = "abcdefg"
print(s)
print(s[0:7:1])
print(s[0:7:2])
print(s[0:7:3])
print(s[0:7:4])


"""The default values in forward direction"""
'''
1. default value for start: 0
2. default value for end: len(s)
3. default value for step: 1
'''

"""Example: 1"""
s = "abcdefg"
print(s)
print(s[0:7:1])
print(s[:7:1])
print(s[0::1])
print(s[0:7:])
print(s[::])


"""Example: 2"""
s = "abcdefg"
print(s)
print(s[-1:-8:-1])
print(s[-1:-8:-2])
print(s[-1:-8:-3])
print(s[-3:-8:-1])

print(s[-1:-8:-1])
print(s[-1:-8:+1])
print(s[-4:-2:+1])


"""The default values backward direction"""
'''
1. default value for start: -1
2. default value for end: -(len(s)+1)
3. default value for step: No default for step
'''

"""Example: 1"""
s = "abcdefg"
print(s)
print(s[-1:-8:-1])
print(s[:-8:-1])
print(s[-1::-1])
print(s[-1:-8:])

"""Example: 2"""
s = "abcdefg"
print(s[::])
print(s[::-1])


################################################# Concatenation of String objects #################################################

"""Example: 1"""
print("abc"+"mno")
print("abc"+str(999))

"""Example: 2"""
fname = input("Enter your first name: ")
lname = input("Enter your last  name: ")
print(fname+" "+lname)


#################################################### String repetition operator ####################################################
print("abc"*2)
print(3*"abc")
print("abc"*int("4"))


############################################### Membership operators in String object ###############################################
"""Example: 1"""
print('a' in 'subrata')
print('b' in 'subrata')
print('c' not in 'subrata')
print('k' not in 'subrata')

"""Example: 2"""
s = 'python is very very easy'
print('java' in s)
print('python' in s)
print('easy' not in s)
print('difficult' not in s)


################################################## Comparing String Objects ##################################################
s1 = input("Enter string1 value: ")
s2 = input("Enter string2 value: ")
if s1==s2:
	print(f"{s1} == {s2}")
elif s1>s2:
	print(f"{s1} > {s2}")
else:
	print(f"{s1} < {s2}")


############################################### Common functions on string objects ###############################################
"""Example: 1"""
s = "subrata"
print(s)
print(len(s))
print(max(s))
print(min(s))
print(sorted(s))
print(sorted(s, reverse=True))

"""Example: 2"""
print(ord('a'))
print(ord('A'))
print(ord('0'))
print(chr(97))
print(chr(65))
print(chr(48))


################################################## String Object is Immutable ##################################################
"""Example: 1"""
s = "python"
print(s)
s.upper()
print(s)

"""Example: 2"""
s = "python"
print(s)
print(s.upper())
print(s)

"""Example: 3"""
s = "python"
print(s)
s= s.upper()
print(s)


##################################################### String specific Methods #####################################################
s = "PYTHON is VeRy eAsY to UNDERstand"
print(s)
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.capitalize())

"""isalnum()"""
print('a'.isalnum())
print('1'.isalnum())
print('$'.isalnum())
print(' '.isalnum())
print(''.isalnum())

"""isalpha()"""
print('a'.isalpha())
print('1'.isalpha())
print('$'.isalpha())
print(' '.isalpha())
print(''.isalpha())

"""isdigit()"""
print('a'.isdigit())
print('1'.isdigit())
print('$'.isdigit())
print(' '.isdigit())
print(''.isdigit())

"""isspace()"""
print('a'.isspace())
print('1'.isspace())
print('$'.isspace())
print(' '.isspace())
print(''.isspace())

"""isupper() & islower()"""
print('a'.islower())
print('A'.islower())
print('a'.isupper())
print('A'.isupper())

"""count()"""
s = "abaabaaabaaaabc"
print(s.count('a'))
print(s.count('b'))
print(s.count('c'))
print(s.count('d'))
print(s.count("ab"))

"""replace()"""
s = "abaabaaabaaaabc"
print(s.replace("ab","k"))
print(s.replace("a","w"))

"""startswith(str) & endswith(str)"""
s = "python is very easy"
print(s.startswith("java"))
print(s.startswith("python"))
print(s.endswith("easy"))
print(s.endswith("difficult"))

"""index(str)"""
s = "abcdefg"
print(s.index('cd'))
print(s.index('fg'))
print(s.index('mn'))

"""find(str)"""
s = "abcdefg"
print(s.find('cd'))
print(s.find('fg'))
print(s.find('mn'))

"""split(seperator)"""
s = "python is very easy"
print(s.split(" "))
print(s.split())

s = "13-10-2023"
print(s.split("-"))

"""seperator.join(L)"""
l = ['python', 'is', 'very', 'easy']
print(' '.join(l))
print('.'.join(l))
print('-'.join(l))