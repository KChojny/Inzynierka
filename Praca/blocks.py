import numpy as np
import file
import dct

def b8x8(A):
    for i in xrange(A.shape[0]/8):
        for j in xrange(A.shape[1]/8):
            block = np.zeros((8,8))
            for k in xrange(8):
                for l in xrange(8):
                    block[k][l] = A[i*8+k][j*8+l] - 128.0
                    block[k][l] = dct.freq(k,l,block)
            #print(block)
            file.save(block,"b/i"+str(i)+"j"+str(j))
