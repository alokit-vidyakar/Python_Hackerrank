#Nested List is comma seperated list of sublist

Empty_Nested_list = []
Nested_list = ['zero index','first index', ['second.zero index','second.first index',['second.second.zero index',
'third.second.first index']]]
print(Nested_list)
print(Nested_list[2])
print(Nested_list[2][2])

#append and insert works same as List
Empty_Nested_list.append('zero index')
Empty_Nested_list.insert(1,'first index')

#now insert and append for nesting
Nested_list[2].append('second.third index')
print(Nested_list[2])

Nested_list[2][2].insert(2,'third.second.second index')
print(Nested_list[2][2])

"""Appending or inserting in a nested list is only possible when there is already a sublist. 
You cannnot change a stand-alone entry into a list.

For instance 
Empty_Nested_list[1].append('first.first index') will throw an error with message: 
The AttributeError: ‘str’ object has no attribute ‘append’ 
""" 
Empty_Nested_list.append(['second.zero index','second.first index',['second.second.zero index','second.second.first index']])
print(Empty_Nested_list)
	