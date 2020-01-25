from VectorClass import Vec
from vectorTasks import zero_vec

D = {'e1', 'e2', 'e3', 'e4'}
vecList = [
    Vec(D, {'e1': 1, 'e2': 4, 'e3': 5}),
    Vec(D, {'e1': 2, 'e2': 0, 'e3': 5, 'e4': 6}),
    Vec(D, {'e1': 1, 'e2': 0, 'e3': 8, 'e4': 0})
    ]

# Quiz 3.1.7: 
# A procedure lin_comb(vlist, clist) with the following spec:
# • input: a list vlist of vectors, a list clist of the same length consisting of scalars
# • output: the vector that is the linear combination of the vectors in vlist with corresponding coefficients clist

def list_comb(vlist, clist): return sum(clist[iter] * vlist[iter] for iter in range(len(vlist)))

# Problem 3.8.1:

# A procedure vec_select using a comprehension for the following computational problem:
# • input: a list veclist of vectors over the same domain, and an element k of the domain
# • output: the sublist of veclist consisting of the vectors v in veclist where v[k] is zero

def vec_select(veclist, k): return [v for v in veclist if v[k] == 0]

# A procedure vec_sum using the built-in procedure sum(·) for the following:
# • input: a list veclist of vectors, and a set D that is the common domain of these vectors
# • output: the vector sum of the vectors in veclist.

def vec_sum(veclist, D) : return sum(veclist, zero_vec(D))

def vec_select_sum(veclist, D, k): return vec_sum(vec_select(veclist, k), D)


print(vec_select_sum(vecList, D, 'e2').f)