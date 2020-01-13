from VectorClass import Vec

# Quiz 3.1.7: 
# a procedure lin_comb(vlist, clist) with the following spec:
# • input: a list vlist of vectors, a list clist of the same length consisting of scalars
# • output: the vector that is the linear combination of the vectors in vlist with corresponding coefficients clist

def list_comb(vlist, clist):
    return sum(clist[iter] * vlist[iter] for iter in range(len(vlist)))