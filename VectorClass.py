# • f, the function, represented by a Python dictionary, and
# • D, the domain of the function, represented by a Python set.
from vectorTasks import add, setItem, getItem

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
        return Vec(self.D, {alpha * item for item in self.f})