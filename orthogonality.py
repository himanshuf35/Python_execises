from VectorClass import Vec
from matutil import mat2coldict, coldict2mat
from dictutil import dict2list, list2dict

def project_along(b, v):
    sigma = (b*v)/(v*v) if v*v > 1e-20 else 0 
    return sigma * v

def project_orthogonal_1(b, v): return b - project_along(b, v)

# • input: a vector b, and a list vlist of mutually orthogonal vectors
# • output: the projection b⊥ of b orthogonal to the vectors in vlist
def project_orthogonal(b, vList): 
    for v in vList:
        b = b - project_along(b, v)
    return b

# • input: a vector b and a list [v0, . . . , vk−1] of mutually orthogonal vectors over the reals 
# • output: the pair (b⊥ , sigmadict)) 
def aug_project_orthogonal(b, vList): 
    sigmaDict = dict()
    for index, v in enumerate(vList):
        sigma = sigma = (b*v)/(v*v) if v*v > 1e-20 else 0
        b = b - (sigma*v)
        sigmaDict[index] = sigma 
    sigmaDict[len(vList)] = 1
    return (b, sigmaDict)

# • A list [v1,v2, v3,......, vn] 
# • output: A list of mutually orthogonal vectors v1∗ , . . . , vn∗ such that Span {v1∗,...,vn∗} = Span {v1,...,vn}
def orthogonalize(vList):
    orthList = list()
    for v in vList:
        orthList.append(project_orthogonal(v, orthList))
    return orthList

def aug_orthogonalize(vlist): 
    vstarlist = []
    sigma_vecs = []
    D = set(range(len(vlist))) 
    for v in vlist:
        (vstar, sigmadict)= aug_project_orthogonal(v, vstarlist) 
        vstarlist.append(vstar)
        sigma_vecs.append(Vec(D, sigmadict))
    return vstarlist, sigma_vecs

# Procedure QR_solve that will return matrix factorization Q, R
def QR_solve(A):
    col_labels = sorted(A.D[1], key=repr)
    Acolms = dict2list(mat2coldict(A), col_labels)
    (Qlist, Rlist) = aug_orthogonalize(Acolms)
    Q = coldict2mat(list2dict(Qlist, col_labels))
    R = coldict2mat(list2dict(Rlist, col_labels))
    return Q, R
