import numpy as np

def vadilating(A, new_A, num):
    if(A.shape[0] % num != 0 or A.shape[1] % num != 0):
        num1 = num - (A.shape[0] % num)
        num2 = num - (A.shape[1] % num)
        new_A = np.zeros((int(A.shape[0] + num1), int(A.shape[1] + num2)))

    return add_col_row(A, new_A, num1, num2)

def add_col_row(A, new_A, num1, num2):
    print("Dodawanie kolumn i wierszy")
    for i in xrange(A.shape[0]+num1):
        for j in xrange(A.shape[1]+num2):
            if(i < A.shape[0] and j < A.shape[1]):
                new_A[i][j] = A[i][j]
            elif(i < A.shape[0] and j >= A.shape[1]):
                new_A[i][j] = A[i][A.shape[1]-1]
            elif(i >= A.shape[0] and j < A.shape[1]):
                new_A[i][j] = A[A.shape[0]-1][j]
            else:
                new_A[i][j] = A[A.shape[0]-1][A.shape[1]-1]
    A = new_A
    return A
