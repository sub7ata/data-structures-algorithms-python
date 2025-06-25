"""Replace list’s item with new value if found"""
lst = [10,20,30,40,50,20,30,40,20]
p = lst.index(20)
lst[p] = 9999
print(lst)

lst = [10,20,30,40,50,20,30,40,20]
lst1 = sorted(lst, reverse=True)
print(lst1)

lst.sort(reverse=True)
print(lst)


# Get the difference between the two Lists
list1 = ['Scott', 'Eric', 'Kelly', 'Emma', 'Smith']
list2 = ['Scott', 'Eric', 'Kelly']

set1 = set(list1)
set2 = set(list2)

list3 = list(set1.symmetric_difference(set2))
print(list3)

# https://pynative.com/useful-python-tips-and-tricks-every-programmer-should-know/


str1 = "SBAA"
str2 = "URT"

l1 = len(str1)
l2 = len(str2)
i = 0
j = 0
new_str = ""
while i <= l1 and j <= l2:
    if i < l1:
        new_str += str1[i]
    if j < l2:
        new_str += str2[j]
    print(i)
    i += 1
    j += 1
print(f"new_str: {new_str}")


s = "A12B09345DHEWXASDR"
s1 = []
s2 = []
for idx, itm in enumerate(s):
    if itm.isalpha():
        print(itm)
        s1.append(itm)
    else:
        s2.append(itm)
s1.sort()
s2.sort()
ss = ''.join(s1)
ss += ''.join(s2)
print(ss)


s = "A1B5C9F4K2C8"
txt = ""
b = ""
for i in s:
    if i.isalpha():
        b = i
    else:
        print(b, end="")
        txt = int(i) * b
print(txt)
        
        
from itertools import zip_longest
a = 'SBAA'
b = 'URT'

lst = list(map(lambda d: (d[0] or '') + (d[1] or ''), zip_longest(a,b)))
print("".join(lst))


# in:a3z3b4 
# out:aaabbbbzz
s = 'a3z3b4'
ch = ''
chs = []
for idx, itm in enumerate(s):
    if itm.isalpha():
        ch = itm
    else:
        chs.append(ch*int(itm))
chs.sort()
print(''.join(chs))

s = 'aaaabbbccz'

prev_char = s[0]
count = 1
result = ''

for char in s[1:]:
    if char == prev_char:
        count += 1
    else:
        result += f'{count}{prev_char}'
        prev_char = char
        count = 1

result += f'{count}{prev_char}'

print(result)


a = 'a4k3b2'
# o = 'aekdbc'
vlu = ''
for ii in a:
    if ii.isalpha():
        vlu += ii
    else:
        l = ord('a')
        vlu += f"{chr(l+int(ii))}"
print(vlu)


# in: 'aaabbbccczzzzffffdddqqqqqqqqqqsstuv'
s = 'aaabbbccczzzzffffdddqqqqqqqqqqsstuv'
lst = []
for itm in s:
    if itm not in lst:
        lst.append(itm)
# print(lst)
print(''.join(lst))
