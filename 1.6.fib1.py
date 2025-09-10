# name: 최윤서
# student id: 2022105751

def fib1(n: int) -> int:
    if (n <= 1):
        return n
    else:
        return fib1(n-1) + fib1(n-2)
    # 피보나치 수 구하기 (재귀적 방법)
    