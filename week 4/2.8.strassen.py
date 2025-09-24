from typing import List, Tuple

class Matrix:
    def __init__(self, mat):
        self.n = len(mat)
        self.matrix = mat
    
    def __add__(self, other):
        mat = [[0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                mat[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(mat)

    def __sub__(self, other):
        mat = [[0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                mat[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return Matrix(mat)

    def __mul__(self, other):
        mat = [[0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    mat[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return Matrix(mat)
            
def partition(n: int, M: Matrix) -> Tuple[Matrix, Matrix, Matrix, Matrix]:
    m = n // 2
    m1 = [[0] * m for _ in range(m)]
    m2 = [[0] * m for _ in range(m)]
    m3 = [[0] * m for _ in range(m)]
    m4 = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            m1[i][j] = M.matrix[i][j] #상좌
            m2[i][j] = M.matrix[i][j+m] #상우
            m3[i][j] = M.matrix[i+m][j] #하좌
            m4[i][j] = M.matrix[i+m][j+m] #하우

    return Matrix(m1), Matrix(m2), Matrix(m3), Matrix(m4)
    
def combine(n: int, M1: Matrix, M2: Matrix, M3: Matrix, M4: Matrix) -> Matrix:
    m = n // 2
    mat = [[0] * n for _ in range(n)]
    for i in range(m):
        for j in range(m):
            mat[i][j] = M1.matrix[i][j] #C11 > 상좌
            mat[i][j+m] = M2.matrix[i][j] #C12 > 상우
            mat[i+m][j] = M3.matrix[i][j] #C21 > 하좌
            mat[i+m][j+m] = M4.matrix[i][j] #C22 > 하우

    return Matrix(mat)
   
def strassen(n: int, A: Matrix, B: Matrix) -> Matrix:
    global threshold

    if n <= threshold:
        return A * B
    else:
        A11, A12, A21, A22 = partition(n, A)
        B11, B12, B21, B22 = partition(n, B)
        
        m = n // 2
        P1 = strassen(m, A11 + A22, B11 + B22)
        P2 = strassen(m, A21 + A22, B11)
        P3 = strassen(m, A11, B12 - B22)
        P4 = strassen(m, A22, B21 - B11)
        P5 = strassen(m, A11 + A12, B22)
        P6 = strassen(m, A21 - A11, B11 + B12)
        P7 = strassen(m, A12 - A22, B21 + B22)

        C11 = P1 + P4 - P5 + P7
        C12 = P3 + P5
        C21 = P2 + P4
        C22 = P1 - P2 + P3 + P6

        return combine(n, C11, C12, C21, C22)

threshold = 1
