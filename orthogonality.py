def project_along(b, v):
    sigma = (b*v)/(v*v) if v*v > 1e-20 else 0 
    return sigma * v

def project_orthogonal_1(b, v): return b - project_along(b, v)