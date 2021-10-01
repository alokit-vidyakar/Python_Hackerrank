#https://www.hackerrank.com/challenges/py-check-strict-superset/problem
set_a = set(map(int, input().split()))
N = int(input())
check = 1
for i in range(0, N):
	
	set_b = set(map(int, input().split()))
	set_b = set_b.difference_update(set_a)
	if not len(set_b) == 0:
		check =0
		
if check ==0:
	print("False")
else:
	print("True")