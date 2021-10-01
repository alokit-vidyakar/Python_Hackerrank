import math
import cmath
"""
Lets read a pre-defined module by python named math which help us perform as many funtionality as possible 
Thre are many functions, let's see them one by one
"""

"""
1. math.acos: returns cosine. Value range from -1 to 1
2. math.acosh: Returns the inverse hyperbolic cosine of a number

Similary for sin and tan
"""
print(math.acos(1))
print(math.asinh(90))
print(math.atan(1))

"""
min, max, abs, pow are basic functionalatiy used which does not require maths module
"""
print(min(4,5))
print(max(4,5))
print(abs(-13))
print(pow(4,5))

"""
sqrt, ceil, floor, pi are basic math module functionality
"""
print(math.sqrt(64))
print(math.ceil(4.34))
print(math.floor(4.34))
print(math.pi)

"""
1. combianation: returns the number of ways picking k unordered outcomes from n possibilities,
without repetition, also known as combinations.

2. degrees: Converts an angle from radians to degrees
3. dist: Returns the Euclidean distance between two points (p and q), where p and q are the coordinates of that point
4. exp: exponential
5. expm1: e^x-1
"""
print(math.comb(7,5)) #7 to choose from 
print(math.degrees(0.52359878))
print(math.dist([0,0],[4,3]))
print(math.exp(3))
print(math.expm1(3))

"""
1. factorial
2. fmod
3. hypot: retuns hypotenuse

"""
print(math.hypot(4,3))

"""
Complex number: A number can be turned to complex by using complex method
They support addition, subtraction, multiplication and division but not comparision 

Phase: The phase of a complex number is the angle between the real axis and the vector representing the imaginary part

"""
s= complex(4+4j)
print(type(s))
print(s.real)
print(s.imag)
print(cmath.phase(s)) # returned value is in radian. 
print(math.degrees(cmath.phase(s)))