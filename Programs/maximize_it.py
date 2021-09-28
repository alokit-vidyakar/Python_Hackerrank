#https://www.hackerrank.com/challenges/merge-the-tools/problem
import itertools    

km= list(map(int, input().split()))
k = km[0]
m = km[1]
inputs = []
fx_values = []
maximum =0 
for i in range(k):
    inputs.append(list(map(int, input().split()))[1:])
    
product_result= list(itertools.product(*inputs))
for sets in product_result:
    sum =0
    for values in sets: 
        sum+= values**2
    modulo = sum%m
    fx_values.append(modulo)
    
for module in fx_values:
    if module>maximum:
        maximum=module
print(maximum)