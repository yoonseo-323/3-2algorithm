from typing import List

def arrsum(n: int, S: List[int]) -> int:
    sum = 0
    for i in range (0,n):
        sum += S[i]
    return sum
