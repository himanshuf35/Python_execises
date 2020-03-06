from VectorClass import Vec
from MatrixClass import Mat
from GF2 import one
from matutil import coldict2mat, listlist2mat, mat2coldict, coldict2mat, rowdict2mat
from vectorTasks import list2vec, zero_vec
from bitutil import str2bits, bits2str, bits2mat, mat2bits, noise
from solver import solve

L = [[0,0,0],[1,0,0],[0,1,0],[1,1,0],[0,0,1],[1,0,1],[0,1,1],[1,1,1]]
corners = [list2vec(v) for v in L]

def line_segment(pt1, pt2, samples=100): return [(i/samples)*pt1 + (1-i/samples)*pt2 for i in range(samples+1)]

def pixel(x): return (x[0], x[1])

def scale_down(x): return list2vec([x[0]/x[2], x[1]/x[2], 1])

# line_segments = [line_segment(corners[i], corners[j]) for i,j in [(0,1),(2,3), (0,2),(1,3),(4,5),(6,7),(4,6),(5,7),(0,4),(1,5),(2,6), (3,7)]]
# pts = sum(line_segments, [])

# shifted_pts = [v+list2vec([1,1,8]) for v in pts]
# xpixels = 100
# ypixels = 100
# cb = [list2vec([1/xpixels,0,0]), list2vec([0,1/ypixels,0]), list2vec([0,0,1])]

# reps = [vec2rep(cb, v) for v in shifted_pts]
# in_camera_plane = [scale_down(u) for u in reps]
# pixels = [pixel(u) for u in in_camera_plane]
# plot(pixels, 30, 1)

# Task 5.12.1: Write a procedure move2board(y) with the following spec:
# • input: a {’y1’,’y2’,’y3’}-vector y, the coordinate representation in whiteboard coor- dinates of a point q
# (Assume q is not in the plane through the origin that is parallel to the whiteboard plane, i.e. that the y3 entry is nonzero.)
# • output: a {’y1’,’y2’,’y3’}-vector z, the coordinate representation in whiteboard coor- dinates of the point p such that the line through the origin and q intersects the whiteboard plane at p.

def move2board(q): return Vec(q.D, {key: q[key]/q['y3'] for key in q.D})

# Task 5.12.2: Define the domain D = R × C.
# Write a procedure make equations(x1, x2, w1, w2) that outputs a list [u, v] consisting
# of two D-vectors u and v such that Equations 5.11 and 5.12 are expressed as
# u·h=0 v·h=0
# where h is the D-vector of unknown entries of H.
R = {'y1', 'y2', 'y3'}
C = {'x1', 'x2', 'x3'}
D = {(y, x) for y in R for x in C }

def make_equations(x1, x2, w1, w2): 
   return[
       Vec(D, {('y3', 'x1'): w1 * x1, ('y3', 'x2'): w1 * x2, ('y3', 'x3'): w1, ('y1', 'x1'): -x1, ('y1', 'x2'): -x2, ('y1', 'x3'): -1}),
       Vec(D, {('y3', 'x1'): w2 * x1, ('y3', 'x2'): w2 * x2, ('y3', 'x3'): w2, ('y2', 'x1'): -x1, ('y2', 'x2'): -x2, ('y1', 'x3'): -1})
   ]

# Task 5.12.3: Write the D-vector w with a 1 in the (’y1’, ’x1’) entry.

topLeft = make_equations(358, 36, 0, 0)
topRight = make_equations(329, 597, 1, 0)
bottomLeft = make_equations(592, 157, 0, 1)
bottomRight = make_equations(580, 483, 1, 1)
w = Vec(D, {('y1', 'x1'): 1})
e = {0, 1, 2, 3, 4, 5, 6, 7, 8}
rowDict = {
    0: topLeft[0],
    1: topLeft[1],
    2: topRight[0],
    3: topRight[1],
    4: bottomLeft[0],
    5:bottomLeft[1],
    6: bottomRight[0], 
    7: bottomRight[1],
    8: w
    }

pyFile = open('tempPy')
print(pyFile.read())
# print(rowDict)
# L1Matrix = rowdict2mat(rowDict)
# bVec = zero_vec(e)
# bVec[8] = 1
# print(L1Matrix.D[0] == bVec.D)
# print(bVec)
# solve(L1Matrix, bVec)
# print(solve) 
# A = Mat(({'a','b'},{'A','B'}), {('a','A'):one, ('a','B'):one, ('b','B'):one})
# b = Vec({'a','b'}, {'a':one})
# x = solve(A, b)
# print(x)
