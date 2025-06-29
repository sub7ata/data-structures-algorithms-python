"""Ex: 1"""
d = {1:"One", 2:"Two", 3:"Three", 4:"Dhoni", 5:"Five"}
print(d) 
print(d.keys()) 
print(d.values())
print(d.items())
print(d.get(2,"NA"))
print(d.get(6,"NA"))

"""Ex: 2"""
d = {i:i*i for i in range(1,11)}
print(d)

"""Ex: 3"""
import math
def isprime1(n):
	factors=0
	for i in range(1,n+1):
		if n%i==0:
			factors=factors+1
	return factors==2

d = {i:math.factorial(i) for i in range(1,11) if not isprime1(i)}
print(d)

"""Ex: 4"""
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

res_dict = dict(zip(keys, values))
print(res_dict)

"""Ex: 5"""
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = {**dict1, **dict2}
print(dict3)

"""Ex: 6"""
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)

"""Ex: 7"""
def count_char_frequencies(input_string):
	frequency_dict = {}
	for char in input_string:
		frequency_dict[char] = frequency_dict.get(char, 0) + 1
	return frequency_dict

string1 = 'Jessa'
print(f"Frequencies for '{string1}': {count_char_frequencies(string1)}")


"""Ex: 8"""
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)


"""Ex: 8"""
def invert_dictionary(input_dict):
    inverted_dict = {}
    for key, value in input_dict.items():
        inverted_dict[value] = key
    return inverted_dict

original_dict1 = {'a': 1, 'b': 2, 'c': 3}

print(f"Original dictionary 1: {original_dict1}")
print(f"Inverted dictionary 1: {invert_dictionary(original_dict1)}")