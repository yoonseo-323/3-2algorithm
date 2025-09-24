from typing import List

def partition(low: int, high: int, S: List[int]) -> int:
    pivotitem = S[low]
    j = low

    for i in range(low + 1, high + 1):
        if (S[i] < pivotitem):
            j += 1
            tmp = S[j]
            S[j] = S[i]
            S[i] = tmp
    pivotpoint = j
    tmp = S[low]
    S[low] = S[pivotpoint]
    S[pivotpoint] = tmp
    return pivotpoint

def quicksort(low: int, high: int, S: List[int]) -> None:
    if low < high:
        n = partition(low, high, S)
        quicksort(low, n-1, S)
        quicksort(n+1, high, S)
