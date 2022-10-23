from functools import lru_cache


@lru_cache
def fib(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-1]+f[i-2])
    return f[n]


@lru_cache
def get_fib(n):
    return 0 if n == 0 else 1 if n < 3 else get_fib(n-1) + get_fib(n-2)

