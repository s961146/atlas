import numpy as np
import math

def find_nodes(mat):
    return np.count_nonzero(mat == math.inf)

def find_nonzero_indexes (mat):
    dict ={}
    for index,x in np.ndenumerate(mat):
        if x != 0 and x != math.inf:
            dict[index[0]]=x
    return dict

def astar_func (n):
    n +=1
    return n