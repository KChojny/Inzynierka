import numpy as np

def alpha(uv): #funkcja do wyliczenia wspolczynnikow
    if(uv != 0):
        return 1
    else:
        return 1/np.sqrt(2)

def cosinus(xy,uv): #funkcja kosinusa
    return np.cos((2*xy+1)*uv*np.pi/16)

def freq(M, DCT): #funkcja dyskretnej transformacji kosinusowej
    for u in xrange(8):
        for v in xrange(8):
            suma = 0.0
            for i in xrange(8):
                for j in xrange(8):
                    suma = suma + cosinus(i,u) * cosinus(j,v) * M[i][j]
            DCT[u][v] = round(0.25 * alpha(u) * alpha(v) * suma)
    return DCT

def ifreq(M, IDCT): #funkcja odwrotnej transformacji kosinusowej
    for i in xrange(8):
        for j in xrange(8):
            suma = 0.0
            for u in xrange(8):
                for v in xrange(8):
                    suma = suma + alpha(u) * alpha(v) * M[u][v] * cosinus(i,u) * cosinus(j,v)
            IDCT[i][j] = round(suma * 0.25)
    return IDCT
