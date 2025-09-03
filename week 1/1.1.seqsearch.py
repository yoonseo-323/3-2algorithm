from typing import List

def seqsearch(n: int, S: List[int], x: int) -> int: 
    location = 0
    flag = 0
    for i in range (0,n):
        if (S[i]==x):
            location = i
            flag += 1
            break
    if (flag == 0):
        location = -1
    
    return location