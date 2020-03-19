from VectorClass import Vec
from cancer_data import read_training_data
from matutil import mat2rowdict, listlist2mat
from vectorTasks import zero_vec, list2vec

(A, b) = read_training_data('train.data')
(C, d) = read_training_data('validate.data')
w = Vec(A.D[1], {key: 0 for key in A.D[1]})

def signum(u): return Vec(u.D, {key: 1 if u[key] >= 0 else -1 for key in u.f})

# the procedure fraction wrong(A, b, w) with the following spec:
# • input: An R×C matrix A whose rows are feature vectors, an R-vector b whose entries are +1 and −1, and a C-vector w
# • output: The fraction of of row labels r of A such that the sign of (row r of A)·w differs from that of b[r].
def fraction_wrong(A, b, w): 
    outputVec = signum(A * w)
    return len([key for key in outputVec.D if outputVec[key] != b[key]]) / len(A.D[0])

# a procedure loss(A, b, w) that takes as input the training data A, b and a hypothesis vector w, 
# and returns the value L(w) of the loss function for input w.
def loss(A, b, w): print(((A * w) - b)*((A * w) - b))

def find_grad(A, b, w):
    rowVecDict = mat2rowdict(A)
    return 2 * (((A * w) - b) * A)
    
# a procedure gradient descent step(A, b, w, sigma) that,
# given the training data A,b and the current hypothesis vector w, returns the next hypothesis vector.
def gradient_descent_step(A, b, w, sigma): 
    return w - (sigma * find_grad(A, b, w))

def gradient_descent(A, b, w, sigma, T): 
    for t in range(T):
        w = gradient_descent_step(A, b, w, sigma)
    return  w


wG = gradient_descent(A, b, w, 0.000000001, 300)
print(fraction_wrong(C, d, w))
print(fraction_wrong(C, d, wG))

