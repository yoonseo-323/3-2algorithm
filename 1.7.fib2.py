# name: 최윤서
# student id: 2022105751

def fib2(n: int) -> int:
    f = [0] * (n + 1)
    if (n > 0):
        f[1] = 1
        for i in range (2, n+1):
            f[i] = f[i-1] + f[i-2]
    # 피보나치 수 구하기 (반복적 방법)
    return f[n]