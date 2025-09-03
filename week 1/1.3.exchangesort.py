from typing import List

def exchangesort(n: int, S: List[int]) -> None:
    temp = 0
    for i in range (0, n):
        for j in range (0, i):
            if (S[j] > S[i]):
                temp = S[j]
                S[j] = S[i]
                S[i] = temp
                temp = 0
