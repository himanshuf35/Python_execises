
# from vectorTasks import add, setItem, getItem

# Quiz 2.7.4: 
# Write a procedure add(u, v) with the following spec:
# • input: instances u and v of Vec
# • output: an instance of Vec that is the vector sum of u and v

def add(u, v): return Vec(u.D, {d: getItem(u, d) + getItem(v,d) for d in u.D})

# Quiz 2.7.2: Write a procedure getitem(v, d) with the following spec:
# • input: an instance v of Vec, and an element d of the set v.D
# • output: the value of entry d of v
def setItem(v, d, val): v.f[d] = val

def getItem(v, d): return v.f[d] if d in v.f else 0

def checkEquality(A, B):
    result = True
    for dictKey in A.D:
        if A[dictKey] != B[dictKey]:
            result = False
            break
    return result

# • f, the function, represented by a Python dictionary, and
# • D, the domain of the function, represented by a Python set.
class Vec:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function

    __add__ = add
    __getitem__ = getItem
    __setitem__ = setItem

    def	__mul__(self, other): 
        if isinstance(other, Vec):
            dot_product = 0
            for key in self.D: 
                if key in self.f and key in other.f :
                    dot_product = dot_product + self.f[key] * other.f[key]
            return dot_product
        else:
            return NotImplemented  #  Will cause other.__rmul__(self) to be invoked

    def __rmul__(self, alpha):
        return Vec(self.D, {alpha * item for item in self.f.values()})

    def __eq__(self, other):
        return self.D == other.D and checkEquality(self, other)

    def __str__(v):
        "pretty-printing"
        D_list = sorted(v.D, key=repr)
        numdec = 3
        wd = dict([(k,(1+max(len(str(k)), len('{0:.{1}G}'.format(v[k], numdec))))) if isinstance(v[k], int) or isinstance(v[k], float) else (k,(1+max(len(str(k)), len(str(v[k]))))) for k in D_list])
        s1 = ''.join(['{0:>{1}}'.format(str(k),wd[k]) for k in D_list])
        s2 = ''.join(['{0:>{1}.{2}G}'.format(v[k],wd[k],numdec) if isinstance(v[k], int) or isinstance(v[k], float) else '{0:>{1}}'.format(v[k], wd[k]) for k in D_list])
        return "\n" + s1 + "\n" + '-'*sum(wd.values()) +"\n" + s2