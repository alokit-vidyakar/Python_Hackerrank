""" tuples are used to store multiple values in one variable.
written in round brackets like set
it is immuatable. Values are not gonna change once assigned. 
Duplicate values are allowed in tupplese unlinke set. Also, items are stored in exact order in tuple
To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
"""

tuple1 = ('item0', 'item1', 89, 89)
print(tuple1)
#for items in tuple1:
	#print(items)

#tuple1[0] = "chnage_item"  # throws error
"""unlike tuple, list values can be changed"""

list1 = ['item0', 'item1', 89]
list1[0]= "change_item0"
print(list1[0])

"""set is created by keyword"""
set1= set(["item0"])
#or 
set2= {'item0', 'item1', 89, 89}
print("set1 is: ",set1)
print("set2 is: ", set2)

"""changing a tuple 
In order to change  tuple, convert that tuple into a list and then modify the list. 
Change the list back into the tuple"""

list1 = list(tuple1)
print(list1)
list1.append("new item added by list")
tuple1 = tuple(list1)
print("chnaged tuple: ", tuple1)

"""We can add two tuple by simply adding them and that is allowed"""
tuple2= ("tuple2 item",)
tuple1+= tuple2
print("after adding tupple 2 in tuple 1: ",tuple1)

"""unpacking of tuple is done which means we are also allowed to extract the values back into variables"""
(a,b,c,d,e,f) = tuple1
print("unpacked values: ",a,b,c,d,e,f)
(A,B, *C) = tuple1
print("Unpacked with star: ", A, B,C)