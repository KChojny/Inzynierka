import numpy as np

def subsampling(A, new_A):
    print("Zmniejszanie rozdzielczosci dla chrominancji")
    for i in xrange(new_A.shape[0]):
        for j in xrange(new_A.shape[1]):
            new_A[i][j] = int((A[2*i][2*j] + A[2*i][2*j+1] + A[2*i+1][2*j] + A[2*i+1][2*j+1])/4)
    return new_A
