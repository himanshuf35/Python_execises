
from VectorClass import Vec
from MatrixClass import Mat
from gf2 import one
from matutil import coldict2mat, listlist2mat, mat2coldict, coldict2mat
from vectorTasks import list2vec, zero_vec
from bitutil import str2bits, bits2str, bits2mat, mat2bits, noise

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

# Task 4.14.1: Create an instance of Mat representing the generator matrix G.
# You can use the procedure listlist2mat in the matutil module.
# Since we are working over GF(2), you should use the value one from the GF2 module to represent 1.

GList = [
    [one, one, 0, one],
    [one, 0, one, one],
    [one, 0, 0, 0],
    [0, one, one, one],
    [0, one, 0, 0],
    [0, 0, one, 0],
    [0, 0, 0, one],
    ]
G = listlist2mat(GList)

RList = [
    [0, 0, one, 0, 0, 0, 0],
    [0, 0, 0, 0, one, 0, 0],
    [0, 0, 0, 0, 0, one, 0],
    [0, 0, 0, 0, 0, 0, one] 
]
R = listlist2mat(RList)

#Hamming Code matrix
HList = [
    [0, 0, 0, one, one, one ,one ],
    [0, one, one, 0, 0, one, one],
    [one, 0, one, 0, one, 0, one]
]
H = listlist2mat(HList)   

# Task 4.14.5:
# A procedure find_error that takes an error syndrome and returns the corresponding error vector e.

def find_error(e2): 
    Hc = H * e2
    hColumnDic = mat2coldict(H)
    errorVector = zero_vec(e2.D)
    for dictKey in hColumnDic: 
        if hColumnDic[dictKey] == Hc:
            errorVector[dictKey] = one
    return errorVector

# Task 4.14.6

def Task_error_vector():
    _c = list2vec([one, 0, one, one, 0, one, one])
    _e = find_error(_c)
    c = _c + _e
    cDecoded = R * c
    print(cDecoded)

# Task 4.14.7
# A one-line procedure find_error_matrix with the following spec:
# • input: a matrix S whose columns are error syndromes
# • output: a matrix whose cth column is the error corresponding to the cth column of S.

def find_error_matrix(S): return coldict2mat({dictKey: find_error(_c) for dictKey, _c in mat2coldict(S).items()})

S = listlist2mat([
    [one, 0],
    [one, 0],
    [one, one],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0]
])

# Task 4.14.8:
# Try out str2bits(str) on the string s defined above, and verify that bits2str(L) gets you back the original string.

s = ''.join([chr(i) for i in range(256)])
b = str2bits(s)


# Task 4.14.9:
# Try converting a string to a list of bits to a matrix P and back to a string, and verify that you get the string you started with.

P = bits2mat(b)
_b = mat2bits(P)
_s = bits2str(_b)

# Task 4.14.10:
# Putting these procedures together, compute the matrix P which represents the string ”I’m trying to free your mind,
#  Neo. But I can only show you the door. You’re the one that has to walk through it.”

s1 = "I’m trying to free your mind,Neo. But I can only show you the door. You’re the one that has to walk through it."
b1 = str2bits(s1)
P1 = bits2mat(b1)
# print(P1)

# Task 4.14.11:
# To simulate the effects of the noisy channel when transmitting your matrix P , use noise(P, 0.02) to create a random matrix E.
# The matrix E + P will introduce some errors. To see the effect of the noise, convert the perturbed matrix back to text.

E = noise(P1, 0.02)
N = P1 + E
_b1 = mat2bits(N)
_s1 = bits2str(_b1)

# Task 4.14.12:
# Encode the words represented by the columns of the matrix P, obtaining a matrix C.

C = G * P1
E1 = noise(C, 0.02)
_C = E1 + C
h = find_error_matrix(_C)

_C1 = h + _C
d = R * _C1
o = mat2bits(d)
_o = bits2str(o)
print(_o)