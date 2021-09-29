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
print(len(dictionary))
print(*(dictionary.values()))