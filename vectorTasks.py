from plotting import plot

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