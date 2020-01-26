
from VectorClass import Vec
from MatrixClass import Mat
from gf2 import one
from matutil import coldict2mat

M=Mat(({'a','b'}, {'@', '#', '?'}), {('a','@'):1, ('a','#'):2, ('a','?'):3, ('b','@'):10, ('b','#'):20, ('b','?'):30})

# Quiz 4.1.1:
# Write a nested comprehension whose value is list-of-row-list representation of a 3 × 4 matrix all of whose elements are zero:

def zero_matrix_rowwise(r, c): return [[0 for i in range(c)] for j in range(r)]

# Quiz 4.1.2: 
# Write a nested comprehension whose value is list-of-column-lists representation of a 3×4 matrix whose i,j element is i−j:

def matrix_columnwise(r, c): return [[i - j for i in range(r)] for j in range(c)]

# Quiz 4.1.8: 
# Write a one-line procedure identity(D) that, given a finite set D,
# returns the D × D identity matrix represented as an instance of Mat.

def identity(D): return Mat((D, D), {(label, label): 1 for label in D})

# Quiz 4.1.9:
# Write a one-line procedure mat2rowdict(A) that, 
# given an instance of Mat, re- turns the rowdict representation of the same matrix. Use dictionary comprehensions.

def mat2rowdict(A): 
    return {rowLabel: Vec(A.D[1], {columnLabel: A.f[(rowLabel, columnLabel)] for columnLabel in A.D[1]}) for rowLabel in A.D[0]}

# Quiz 4.1.10: 
# Write a one-line procedure mat2coldict(A) that, given an instance of Mat,
# returns the coldict representation of the same matrix. Use dictionary comprehensions.

def mat2coldict(A): 
    return {columnLabel: Vec(A.D[0], {rowLabel: A.f[(rowLabel, columnLabel)] for rowLabel in A.D[0]}) for columnLabel in A.D[1]}

# Quiz 4.3.1: 
# The procedure mat2vec(M) that, given an instance of Mat, returns the cor- responding instance of Vec.

def mat2vec(M): return Vec({(rowLabel, columnLabel) for rowLabel in M.D[0] for columnLabel in M.D[1]}, M.f)

# Quiz 4.4.2: 
# Write the procedure transpose(M) that, given an instance of Mat representing a matrix,
# returns the representation of the transpose of that matrix.

def transpose(M): return Mat((M.D[1], M.D[0]), {(rowL, columnL): v for (columnL, rowL), v in M.f.items()})

def button_vectors(n):
    D = {(i,j) for i in range(n) for j in range(n)} 
    vecdict = {(i,j) : Vec(D,dict([((x,j),one) for x in range(max(i-1,0), min(i+2,n))] + [((i,y),one) for y in range(max(j-1,0), min(j+2,n))]))for (i,j) in D}
    return vecdict

B = coldict2mat(button_vectors(2))

print(B.f)