# name: 최윤서
# student id: 2022105751
from typing import List

def matrixmult(n: int, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    C = [[0] * n for _ in range(n)]
    for i in range (n):
        arr = A[i]  # A 배열이 [[]] 형태로, 각 행을 받는 열을 만들어 행렬의 곱셈 진행
        for j in range (n):
            for k in range (n):
                C[i][j] += arr[k]*B[k][j]
    

    return C
