import time

def bin2(n: int, k: int) -> int:
    B = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range (0, n+1):
        for j in range (0, min(i, k)+1):
            if (j == 0 or j == i):
                B[i][j] = 1
            else:
                B[i][j] = B[i-1][j-1] + B[i-1][j]
    return B[n][k]
