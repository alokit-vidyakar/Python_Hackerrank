#saves multiple item in one varibale which are unique and are unordered and unindexed
#do not support repetiiton of item and are unchangable. 

#creating an empty set using constrctor 
empty_set= set()
non_empty_set= {"a", "b", 'c'}
print(non_empty_set) #order of item during print is not same

#len function is used to get the length of the set 
print("length of non_empty_set is: ",len(non_empty_set))

#iterating in set 
for items in non_empty_set:
	print(items)

#adding in set. Only one item at a time
empty_set.add(True)
print("after addition empty set is:",empty_set)

"""#equalizing two different set. Older entries are forgt and both set values become euqual
empty_set=non_empty_set
print(empty_set)"""

#add items of one set in another. Here items of non-empty set are added in empty set
empty_set.update(non_empty_set)
print("updated set is :", empty_set)

#removing item from set. If item does not exist then ERROR occurs
empty_set.remove("b")
print(empty_set)

#remove item from set using discard. If item does not exist then NO ERROR occurs
empty_set.discard(False)
print("after discard of non-available item:",empty_set)

#pop the list item from set just like list 
empty_set.pop()
print("after popping from empty set",empty_set)

#delete the set completely 
#del empty_set
#print(empty_set) #throws error because no such set exist now


"""SET ACTIONS LIKE UNION INTERSECTION ASSYMETRIC """

"""UNION methods are used two return a set which conains all the item from both set. Non-repetitve. This is same as Update"""
union_set = empty_set.union(non_empty_set)
print('non_empty_set is: ', non_empty_set)
print('empty set is:', empty_set)
print('union set is: ', union_set)

"""Intersection update is where common items are added only"""
intersection_set= empty_set.intersection(non_empty_set)
print("Common items by intersection are: ",intersection_set)


"""symmetric difference update is method by which we keep items which are not available in both sets"""
symmetric_difference_set= non_empty_set.symmetric_difference(empty_set)
print("different items by symmetric_difference are: ",symmetric_difference_set)

"""difference is the method which returns items a set as a result. This returned set contains items which are present in calling 
set but not in parameter set"""
difference_set= non_empty_set.difference(empty_set)
print("Items present in non_empty_set but not in empty_set: ",difference_set)



"""Other functions which are available in set are:
1. clear: removed all the elemets of the set
2. isdisjoint(): Returns whether two sets have a intersection or not
3. issubset(): Returns whether another set contains this set or not
"""