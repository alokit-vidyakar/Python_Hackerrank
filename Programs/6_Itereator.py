import itertools
#from itertools import product


"""
An iterator is an object that can be used to iterate through an object. 

First is iter() function which makes maps an iterator with any iterable object such as list, String, set, tuples, dictionary 
"""
list1 = ['alokit','bishu','chaitanya']
iterator = iter(list1)
print(iterator)
"""Printing itirator is like printing a map. Give pointor to object. 
Like for printing a map we need it to convert it to a list as below
"""
mymap1=map(int, "5,6,7".split(','))
"""print(mymap1)
print(*mymap1)
"""
print(next(iterator))
"""strings can be iterated too """
String = "Alokit"
iterator = iter(String)
itertor = next(iterator)
print(next(iterator))

"""Zip fucntion is used to merge two or more lists"""
mymap1=list(mymap1)
zipped_list= zip(list1,mymap1)
print("zipped list is: ", *zipped_list)

"""
methods in iterator tool
1. count(start, step)
"""
for i in itertools.count(10,5):
	print(i)
	if i == 55:
		break
"""
2.Product: This is used to produce a cartesian product of input iterables. 
There is optional argumnent "repeat" if want to find product with same set 
 
"""
print("\n\n\n***********product***************")
print(*itertools.product(list1, repeat=2))
#print(*itertools_list)
print(*itertools.product(list1,mymap1))
#print(*itertools_list)

print("\n\n\n***********Permutation***************")
"""
3. Permutation: Genrate all possible purmuation of an iterarble. 
The position of the item matters more than the value
Accept two arguments, iterable and group-size

If group size is not given then by-deault value is length of iterable 
In the given example, permutations(list1,3) = permutations(list1)
"""
print(*itertools.permutations(list1,2))
print(*itertools.permutations(range(4),3))

