#https://www.hackerrank.com/challenges/no-idea/problem
nm = list(map(int, input().split()))
n = nm[0]
m = nm[1]
array = list(map(int, input().split()))
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))
happiness=0	
for arr in array:
	if arr in set_a:
		happiness+=1
	if arr in set_b:
		happiness-=1
print(happiness)

"""
Other way is:
	
print(sum((i in A)- (i in B) for i in array))
"""