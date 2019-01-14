import numpy as np

def YCbCr(A,B,C,D):
    print("Zapisywanie wartosci do macierzy")
    for i in xrange(A.shape[0]):
        for j in xrange(A.shape[1]):
            B[i][j] = int(A[i][j][0]*0.299+A[i][j][1]*0.587+A[i][j][2]*0.114)
            C[i][j] = int(128-A[i][j][0]*0.168739-A[i][j][1]*0.331264+A[i][j][2]*0.5)
            D[i][j] = int(128+A[i][j][0]*0.5-A[i][j][1]*0.418688-A[i][j][2]*0.081312)

    return B, C, D
