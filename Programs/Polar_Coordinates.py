#https://www.hackerrank.com/challenges/polar-coordinates/problem
#for git 
import math
import cmath
s = complex(input())
print(math.sqrt(pow(s.real,2)+pow(s.imag,2)))
print(cmath.phase(s))