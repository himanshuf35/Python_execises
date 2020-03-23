# Copyright 2013 Philip N. Klein
def dict2list(dct, keylist): 
    # print(len(dct.keys()))
    # print(len(keylist))
    # assert set(dct.keys()) == keylist
    return [dct[key] for key in keylist]

def list2dict(L, keylist): 
    assert len(L) == len(keylist)
    return {list(keylist)[itr]: L[itr] for itr in range(len(L))}
