import numpy as np

def tables(Q, YC, QL):
    if(YC == 'Y'): #tablice kwantyzacji dla luminancji
        Q = [
        [16, 11, 10, 16, 24, 40, 51, 61],
        [12, 12, 14, 19, 26, 58, 60, 55],
        [14, 13, 16, 24, 40, 57, 69, 56],
        [14, 17, 22, 29, 51, 87, 80, 62],
        [18, 22, 37, 56, 68, 109, 103, 77],
        [24, 35, 55, 64, 81, 104, 113, 92],
        [49, 64, 78, 87, 103, 121, 120, 101],
        [72, 92, 95, 98, 112, 100, 103, 99]
        ]
    else: #tablice kwantyzacji dla chrominancji
        Q = [
        [17, 18, 24, 47, 24, 40, 51, 61],
        [18, 21, 26, 66, 26, 58, 60, 56],
        [24, 26, 56, 99, 99, 99, 99, 99],
        [47, 99, 99, 99, 99, 99, 99, 99],
        [99, 99, 99, 99, 99, 99, 99, 99],
        [99, 99, 99, 99, 99, 99, 99, 99],
        [99, 99, 99, 99, 99, 99, 99, 99],
        [99, 99, 99, 99, 99, 99, 99, 99]
        ]

    if(QL < 50 and QL >= 1): #ustalanie poziomu jakosci
        for i in xrange(8):
            for j in xrange(8):
                Q[i][j] = np.minimum(Q[i][j] * (50/QL), 255)
    elif(QL > 50 and QL < 100):
        for i in xrange(8):
            for j in xrange(8):
                Q[i][j] = np.minimum(Q[i][j] * (2-(QL/50)), 255)
    return Q

def quantization(M, Q): #funkcja kwantyzacji
    for i in xrange(8):
        for j in xrange(8):
            M[i][j] = round(M[i][j]/Q[i][j], 0)

    return M

def dequantization(M, Q): #funkcja dekwantyzacji
    for i in xrange(8):
        for j in xrange(8):
            M[i][j] = M[i][j] * Q[i][j]

    return M
