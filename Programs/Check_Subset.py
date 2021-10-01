#https://www.hackerrank.com/challenges/py-check-subset/problem
test_case = int(input())

for i in range(0,test_case):
	na = int(input())
	set_a = set(map(int,input().split()))
	nb = int(input())
	set_b = set(map(int,input().split()))

	set_differece = set_a.difference(set_b)
	if len(set_differece)==0:
		print("True")
	else:
		print("False")	