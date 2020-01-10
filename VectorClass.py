# • f, the function, represented by a Python dictionary, and
# • D, the domain of the function, represented by a Python set.
class Vec:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function

    def	__mul__(self, other): 
        dot_product = 0
        for key in self.D: 
            if key in self.f and key in other.f :
                dot_product = dot_product + self.f[key] * other.f[key]
        return dot_product

    def __getitem__(self, key):
        return self.f[key]
    
    def __setitem__(self, key, value):
        self.f[key] = value