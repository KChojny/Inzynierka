import numpy as np
import tables

def matrix2array(M,A):
    rows = M.shape[0]
    columns = M.shape[1]
    k=0
    solution=[[] for i in xrange(rows+columns-1)]

    for i in xrange(rows):
        for j in xrange(columns):
            sum=i+j
            if(sum%2 == 0):
                solution[sum].insert(0,M[i][j])
            else:
                solution[sum].append(M[i][j])
    for i in solution:
        for j in i:
            A[k] = j
            k += 1
    return A

def separationDC(A):
    DC = A[0]
    return DC

def separationAC(A):
    AC = np.zeros((63))
    for i in xrange(63):
        AC[i] = A[i+1]
    return AC

def connectionACDC(DC,AC):
    A = np.zeros((64))
    A[0] = DC
    for i in xrange(63):
        A[i+1] = AC[i]
    return A

def DC2diff(DC):
    diff = np.zeros((DC.shape[0]))
    diff[0] = DC[0]
    for i in xrange(DC.shape[0] - 1):
        diff[i+1] = DC[i+1] - DC[i]
    return diff

def diff2DC(diff):
    DC = np.zeros((diff.shape[0]))
    DC[0] = diff[0]
    for i in xrange(diff.shape[0] - 1):
            DC[i+1] = diff[i+1] + DC[i]
    return DC

def dec2bin(x):
    code = ""
    if(x != 0):
        y = x
        if(x < 0):
            y = abs(y)
        while(y != 0):
            code = str(y%2) + code
            if(y%2 == 1):
                y -= 1
            y /= 2
        if(x < 0):
            c = ""
            for i in xrange(len(code)):
                if(code[i] == str(1)):
                    c +=  '0'
                else:
                    c += '1'
            code = c
    return code

def compresionDC(file, DC):
    for i in DC:
        diff = dec2bin(DC[i],2)
        size = tables.SSSS(len(diff))
        out = str(ssss) + diff
        file.write(out)
    return file
