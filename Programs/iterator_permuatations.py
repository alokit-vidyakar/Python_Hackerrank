#https://www.hackerrank.com/challenges/itertools-permutations/problem
import itertools
input_string = list(map(str, input().split()))
string = input_string[0]
size = int(input_string[1])
answer = []

permutations = itertools.permutations(string,size)
for permutation in permutations:
    value = ''.join(permutation)
    answer.append(value)

answer = sorted(answer)
for ans in answer:
    print(ans)
