import numpy as np

def subsampling(M): #funkcja podprobkowania
    print("Zmniejszanie rozdzielczosci dla chrominancji")
    new_M = np.zeros((int(M.shape[0]/2), int(M.shape[1]/2)))
    for i in xrange(new_M.shape[0]):
        for j in xrange(new_M.shape[1]):
            new_M[i][j] = round((M[2*i][2*j] + M[2*i][2*j+1] + M[2*i+1][2*j] + M[2*i+1][2*j+1])/4)
    return new_M

def oversumpling(M): #funkcja nadprobkowania
    print("Zwiekszanie rozdzielczosci dla chrominancji")
    new_M = np.zeros((int(M.shape[0] * 2), int(M.shape[1] * 2)))
    for i in xrange(M.shape[0]):
        for j in xrange(M.shape[1]):
            new_M[2*i][2*j] = M[i][j]
            new_M[2*i][2*j+1] = M[i][j]
            new_M[2*i+1][2*j] = M[i][j]
            new_M[2*i+1][2*j+1] = M[i][j]
    return new_M
