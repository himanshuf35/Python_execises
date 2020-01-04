from plotting import plot
from image import file2image
import math

#Task 1.4.10
data = file2image('img01.png')
data = reversed(data)
dataList = {x+(y*1j) for y,item in enumerate(data) for x,yItem in enumerate(item) if list(yItem)[0] <= 120}
plot(dataList, 255, 1)

#Task 1.4.12
plot({ (1/2 * z) * 1j for z in dataList}, 255, 1)

#Task 1.4.17
eulerList = [pow(math.e, (2 * math.pi * 1j) / n) for n in range(1,20)]
plot(eulerList)

#Task 1.4.18
S = {2 + 2j,3 + 2j,1.75 + 1j,2 + 1j,2.25 + 1j,2.5+1j,2.75+1j,3+1j,3.25+1j}
plot({ z * (pow(math.e, ( (math.pi/4) * 1j))) for z in S})

#Task 1.4.20
def recenterOrigin(z): return (z.real - 83) + ((z.imag - 95) * 1j)
plot({(recenterOrigin(z) * (pow(math.e, ( (math.pi/4) * 1j)))) * 0.5 for z in dataList}, 190, 1)

#Problem 1.7.1
# input: list of numbers and a positive integer.
# output: list of numbers not containing a multiple of num.
def my_filter(L, num): return [ ele for ele in L if ele % num != 0]

#Problem 1.7.2
# input: list L of non-negative integers.
# output: a list of lists: for every element x in L create a list containing 1, 2, . . . , x.
def my_Lists(L): return [ [x for x in range(1, ele+1)] for ele in L ]

# Problem 1.7.3: my function composition(f,g)
# input: two functions f and g, represented as dictionaries, such that g ◦ f exists.
# output: dictionary that represents the function g ◦ f .
def my_function_composition(f,g): return {fKey: g[f[fKey]] for fKey in f if f[fKey] in g}

# Problem 1.7.12: Write a procedure transform(a,b, L) with the following spec:
# • input: complex numbers a and b, and a list L of complex numbers
# • output: the list of complex numbers obtained by applying f(z) = az + b to each complex number in L
def transform(a, b, L): return[ (a * z) + b for z in L]