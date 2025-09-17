from typing import List

def merge(h: int, m: int, U: List[int], V: List[int], S: List[int]) -> None:
    assert sorted(U) == U
    assert sorted(V) == V
    
    i = j = k = 0
    while (i < h and j < m):
        if (U[i] < V[j]):
            S[k] = U[i]
            i += 1
        else:
            S[k] = V[j]
            j += 1
        k += 1
    if (i > h):
        while (j < m):
            S[k] = V[j]
            k += 1
            j += 1
    else:
        while (i < h):
            S[k] = U[i]
            k += 1
            i += 1

def mergesort(n: int, S: List[int]) -> None:
    h = n // 2
    m = n - h
    if n > 1:
        for i in range(h):
            U[i] = S[i]
        for j in range(m):
            V[j] = S[j+h]
        mergesort(h, U)
        mergesort(m, V)
        merge(h, m, U, V, S)