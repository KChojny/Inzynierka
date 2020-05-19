def save(M, name):
    f = open(name + ".txt","w")
    for i in xrange(M.shape[0]):
        for j in xrange(M.shape[1]):
            f.write(str(M[i][j]) + ' ')
        f.write('\n')
    f.close()
    print("Zapisano  wartosci " + name)

def save1d(A, name):
    f = open(name + ".txt","w")
    for i in xrange(A.shape[0]):
        f.write(str(A[i]) + ' ')
    f.close()
    print("Zapisano  wartosci " + name)
