import numpy as np

import file
import dct
import quantization
import entropy_encoding

def encoding(A,YC,QT,DC,AC):
    print("Kompresja macierzy")
    for i in xrange(A.shape[0]/8):
        for j in xrange(A.shape[1]/8):

            block = np.zeros((8,8))
            for k in xrange(8):
                for l in xrange(8):
                    block[k][l] = A[i*8+k][j*8+l] - 128.0
            file.save(block,"block/i"+str(i)+"j"+str(j))

            DCT = dct.freq(block, np.zeros((8,8)))
            file.save(DCT,"dct/i"+str(i)+"j"+str(j))

            block = quantization.q(DCT, QT)
            file.save(block,"q/i"+str(i)+"j"+str(j))

            array = entropy_encoding.matrix2array(block, np.zeros((64)))
            file.save1d(array,"array/i"+str(i)+"j"+str(j))

            DC[i * int(A.shape[0] / 8) + j] = array[0]
            AC[i * int(A.shape[0] / 8) + j] = separationAC(array)
