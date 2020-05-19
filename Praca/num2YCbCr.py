import numpy as np

def YCbCr(I,Y,Cb,Cr):
    print("Zapisywanie wartosci do macierzy na model barw YCbCr")
    for i in xrange(I.shape[0]):
        for j in xrange(I.shape[1]):
            Y[i][j] = round(I[i][j][0]*0.299+I[i][j][1]*0.587+I[i][j][2]*0.114, 0)
            Cb[i][j] = round(128-I[i][j][0]*0.1687-I[i][j][1]*0.3312+I[i][j][2]*0.5, 0)
            Cr[i][j] = round(128+I[i][j][0]*0.5-I[i][j][1]*0.4187-I[i][j][2]*0.0813, 0)

    return Y, Cb, Cr

def RGB(I,Y,Cb,Cr):
    print("Zapisywanie wartosci do macierzy na model barw RGB")
    for i in xrange(Y.shape[0]):
        for j in xrange(Y.shape[1]):
            I[i][j][0] = round(Y[i][j]+1.402*(Cr[i][j]-128), 0)
            I[i][j][1] = round(Y[i][j]-0.34414*(Cb[i][j]-128)-0.71414*(Cr[i][j]-128), 0)
            I[i][j][2] = round(Y[i][j]+1.772*(Cb[i][j]-128), 0)

    return I
'''
def YCbCrInt(I,Y,Cb,Cr):
    print("Zapisywanie wartosci do macierzy na model barw YCbCr")
    for i in xrange(I.shape[0]):
        for j in xrange(I.shape[1]):
            Y[i][j] = 0.25*I[i][j][0]+0.5*I[i][j][1]+0.25*I[i][j][2]
            Cb[i][j] = I[i][j][0]-I[i][j][2]
            Cr[i][j] = I[i][j][0]-I[i][j][1]

    return Y, Cb, Cr

def RGBInt(I,Y,Cb,Cr):
    print("Zapisywanie wartosci do macierzy na model barw RGB")
    for i in xrange(Y.shape[0]):
        for j in xrange(Y.shape[1]):
            I[i][j][1] = round(Y[i][j]-(0.25*Cb[i][j]+0.25*Cr[i][j]), 0)
            I[i][j][0] = Cb[i][j]+I[i][j][1]
            I[i][j][2] = Cr[i][j]+I[i][j][1]

    return I
'''
