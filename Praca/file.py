def save(M, name):
    f = open(name + ".txt","w")
    for i in xrange(M.shape[0]):
        for j in xrange(M.shape[1]):
            f.write(str(M[i][j]) + ' ')
        f.write('\n')
    f.close()
    print("Zapisano  wartosci " + name)
