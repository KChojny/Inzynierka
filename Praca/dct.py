import numpy as np

def alpha(k):
    if(k != 0):
        return 1
    else:
        return 1/np.sqrt(2)

def beta(k, p):
    return np.cos((2*k+1)*(np.pi*p/16))

def freq(u, v, matrix):
    suma = 0.0
    for i in xrange(8):
        for j in xrange(8):
            suma = suma + alpha(i)*alpha(j)*beta(i,u)*beta(j,v)*matrix[i][j]
    suma = suma / 4
    return suma
