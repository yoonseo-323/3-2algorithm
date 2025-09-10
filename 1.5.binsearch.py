# name: 최윤서
# student id: 2022105751
from typing import List

def binsearch(n: int, S: List[int], x: int) -> int:
    low, high = 0, n - 1
    location = -1
    while (low <= high and location == -1):
        mid = (low+high)//2  # python의 경우 /: 몫 = 실수형, //: 몫 = 정수형
        if (x == S[mid]):
            location = mid
        elif (x < S[mid]):
            high = mid - 1
        else:
            low = mid + 1
    

    return location