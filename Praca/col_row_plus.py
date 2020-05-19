import numpy as np

def validation(M, num):
    print("Walidacja ilosci kolum i wierszy")
    if(M.shape[0] % num != 0 or M.shape[1] % num != 0):
        num1, num2 = 0, 0
        if(M.shape[0] % num != 0):
            num1 = num - (M.shape[0] % num)
        if(M.shape[1] % num != 0):
            num2 = num - (M.shape[1] % num)
        return add_col_row(M, num1, num2)

def add_col_row(M, num1, num2):
    print("Dodawanie kolumn i wierszy")
    new_M = np.zeros((int(M.shape[0] + num1), int(M.shape[1]+ num2)))
    for i in xrange(M.shape[0]+num1):
        for j in xrange(M.shape[1]+num2):
            if(i < M.shape[0] and j < M.shape[1]):
                new_M[i][j] = M[i][j]
            elif(i < M.shape[0] and j >= M.shape[1]):
                new_M[i][j] = M[i][M.shape[1]-1]
            elif(i >= M.shape[0] and j < M.shape[1]):
                new_M[i][j] = M[M.shape[0]-1][j]
            else:
                new_M[i][j] = M[M.shape[0]-1][M.shape[1]-1]
    M = new_M
    return M
