#https://www.hackerrank.com/challenges/word-order/problem
n = int(input())
words=[]
dictionary={}
for i in range(n):
	words.append(input())
for arr in words:
	if arr in dictionary:
		value = dictionary[arr]
		value+=1
		dictionary[arr]=value
	else:
		dictionary[arr]=1
differnt = set()
print(dictionary)
for arr in dictionary:
	differnt.add(arr)
print(len(differnt))
second =[]
for arr in dictionary:
	second.append(dictionary[arr])
print(*second)