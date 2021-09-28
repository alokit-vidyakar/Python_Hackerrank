#playing with lists here

lists = ["first", "second", "third"]
print(lists)
print("Printing items with *: ", *lists)
print("first item in list is: ",lists[0].title())

#sorting in reverse
lists.sort(reverse = True)
print("Welecome to the list in reverse order: ", lists[0],"," ,lists[1],",", lists[2])


if __name__ == '__main__':
	lists[0]="fourth"
print('first item is changed to:', lists[0])


#in list, value change be changed inside function as well
def changeValueOfList():
	lists[0]="third"
changeValueOfList()
print('first item is changed back to: ', lists[0])

#appending the value of list. Must append in order to add new item 
def addValueOfList():
	global lists
	a = input()
	lists.append(a)

addValueOfList()
print(lists)

def addValueOfList(index):
	a= input()
	lists.insert(index, a)
addValueOfList(0)
print(lists)

def removeItemfromList(index):
	del lists[index]
removeItemfromList(0)
print(lists)

for listss in lists:
	print(f"{listss.title()}, is {lists.co}")

def popItemFromList(index):
	lists.pop(index)
def popItemFromList():
	lists.pop()
popped_item=popItemFromList()
print("final list is:",lists)
