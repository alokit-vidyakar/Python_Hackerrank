#https://www.hackerrank.com/challenges/py-set-mutations/problem
_, set_a = int(input()), set(map(int,input().split()))
number_of_other_set = int(input())

for i in range (0,number_of_other_set):
	command, set_b = input().split()[0],set(map(int,input().split()))
	getattr(set_a,command)(set_b)

print(sum(set_a))