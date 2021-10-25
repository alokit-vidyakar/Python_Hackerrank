"""

Pyhon is object oriented programming. 
We can create class, it's attributes, functions are access them using object  
"""

class ReadingClass1:
	name = "Alokit"

ReadingObject = ReadingClass1()
print(ReadingObject.name)

"""
Now we can create a constructor while creating an object. 
This method is called __init__().This init take two positional paramter. 
First argumnent defines name to reference the current class. The reference can be termed anything.
Rest are arguments which are passed.
Here pointer is self. Later I changed it to classPointer
"""
class ReadingClass:
	no_roll_number =0
	def __init__(classPointer,name,rollNumber):
		classPointer.name= name
		classPointer.rollNumber=rollNumber
	def forsuper():
		print("I am super")

ReadingObject = ReadingClass("alokit2",7)
print(ReadingObject.name)
	
	

"""
class definition cannot be empty but if for some reason it is required then we use pass keyword for it
"""
class Passing:
	pass

"""
Inheritance is the way by which one class can inherit the properties of other class. 
The properties and fucntions are inherited by child class. 
Use keyword pass, if want no new function in child class 
"""

class child1(ReadingClass):
	def __init__(childPointer,name):
		childPointer.name=name

child1Object = child1("Alokit_child_class")
print(child1Object.name)
print(child1Object.no_roll_number)
#child1Object.forsuper() #thows error


class child2(ReadingClass):
	pass 
child2Object = child2("alokit", 29)
print(child2Object.name)
print(child2Object.rollNumber)

"""
Super() is used wheb child needs to inher
"""
class superChid(ReadingClass):
	def forsuper():
		super().forsuper()

superChidOject = superChid("superAlokit", 12)
print(superChidOject.name,superChidOject.rollNumber)
superChidOject.forsuper()