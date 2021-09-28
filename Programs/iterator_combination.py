#https://www.hackerrank.com/challenges/itertools-combinations/problem
import itertools
inputs_value = list(map(str, input().split()))
string = inputs_value[0]
size = int(inputs_value[1])
answer = []
string = sorted(string)
for i in range(1,size+1):
    combinations = itertools.combinations(string,i)
    for combination in combinations:
        answer.append(combination)
temp=[]
for ans in answer: 
    joined = ''.join(ans)
    temp.append(joined)
final = []

length = 1
for i in range(1, len(temp)+1):
    for temps in temp:
        if len(temps)==i :
            final.append(temps)
for printing in final:
    print(printing)
