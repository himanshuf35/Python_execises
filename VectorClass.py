# • f, the function, represented by a Python dictionary, and
# • D, the domain of the function, represented by a Python set.
class Vec:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function
