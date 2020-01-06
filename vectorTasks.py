from plotting import plot
from VectorClass import Vec
# Quiz 2.4.2: Write the translation “go east one mile and north two miles” as a function
#  from 2-vectors to 2-vectors, using vector addition. Next, show the result of applying
#  this function to the vectors [4, 4] and [−4, −4].

translationVector = [1, 2]
L = [[2, 2], [3, 2], [1.75, 1], [2, 1], [2.25, 1], [2.5, 1], [2.75, 1], [3, 1], [3.25, 1]]
def addVector(v, vT): return [ v[iter] + vT[iter] for iter in range(len(v))] 
addVector([-4, -4], translationVector)
addVector([4, 4], translationVector)

# Task 2.4.3:
# Enter the procedure definition for 2-vector addition,
#  and use a comprehension to plot the points obtained from L by adding [1, 2] to each:
plot([addVector(v, translationVector) for v in L], 4)

# Quiz 2.5.3: 
# Suppose we represent n-vectors by n-element lists. 
# Write a procedure scalar_vector_mult(alpha, v) that multiplies the vector v by the scalar alpha.

def scalar_vector_mult(alpha, vector): return [ alpha * vectorElement for vectorElement in vector]

# Task 2.5.4: 
# Plot the result of scaling the vectors in L by 0.5,
# then plot the result of scaling them by -0.5.

plot([scalar_vector_mult(0.5, vector) for vector in L])
plot([scalar_vector_mult(-0.5, vector) for vector in L])

# Task 2.6.9:
# python procedure segment(pt1, pt2) that, given points represented as 2-element lists,
# returns a list of a hundred points spaced evenly along the line segment whose endpoints are the two points
# Plot the hundred points resulting when pt1 = [3.5, 3] and pt2 = [0.5, 1]

def segement(pt1, pt2): return [addVector(scalar_vector_mult(alpha, pt1), scalar_vector_mult(1-alpha, pt2)) for alpha in [num/100 for num in range(100)]]
tempList = segement([3.5, 3], [0.5,1])

# Quiz 2.7.1: Write a procedure zero_vec(D) with the following spec:
# • input: a set D
# • output: an instance of Vec representing a D-vector all of whose entries have value zero

def zero_vec(D): return Vec(D, {d:0 for d in D})

# Quiz 2.7.2: Write a procedure getitem(v, d) with the following spec:
# • input: an instance v of Vec, and an element d of the set v.D
# • output: the value of entry d of v
def setItem(v, d, val): v.f[d] = val
def getItem(v, d): return v.f[d] if d in v.f else 0

# Quiz 2.7.3: Write a procedure scalar_mul(v, alpha) with the following spec:
# • input: an instance of Vec and a scalar alpha
# • output: a new instance of Vec that represents the scalar-vector product alpha times v.

def scalar_mul(v, alpha): return Vec(v.D, {d: alpha * v.f[d] for d in v.f})

# Quiz 2.7.4: 
# Write a procedure add(u, v) with the following spec:
# • input: instances u and v of Vec
# • output: an instance of Vec that is the vector sum of u and v

def add(u, v): return Vec(u.D, {d: getItem(u, d) + getItem(v,d) for d in u.D})

# Quiz 2.7.5:
# Write a Python procedure neg(v) with the following spec: 
# • input: an instance v of Vec
# • output: a dictionary representing the negative of v

def neg(v): return Vec(v.D, {d: -v.f[d] for d in v.f})

# Quiz 2.9.4: 
# Write a procedure list_dot(u, v) with the following spec:
# • input: equal-length lists u and v of field elements
# • output: the dot-product of u and v interpreted as vectors

def list_dot(u, v): return sum( [u[iter] * v[iter] for iter in range(len(u))])

# Quiz 2.9.15:
# Write a procedure dot_product_list(needle,haystack) with the following spec:
# • input: a short list needle and a long list haystack, both containing numbers
# • output: a list of length len(haystack)-len(needle) such that entry i of the output list equals the dot-product of the needle with the equal-length sublist of haystack starting at position i

def dot_product_list(needle,haystack): 
    return [ list_dot(needle, haystack[i: i + len(needle)]) for i in range(len(haystack) - len(needle) + 1)]