import math


def get_dividers(n):
    left, right = [], []
    for i in range(1, math.floor(math.sqrt(n))):
        if n % i == 0:
            left.append(i)
            right.append(n // i)
    if math.sqrt(n) % 10 == 0:
        right.pop()
    right.reverse()
    result = left + right
    return result


def is_prime(n):
    for i in range(1, math.floor(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


def get_prime_numbers(n):
    sieve = [True for _ in range(0, n + 1)]
    # sieve[0], sieve[1] = False, False
    for i in range(2, math.floor(math.sqrt(n))):
        if sieve[i]:
            for j in range(i ** 2, n + 1, i):
                sieve[j] = False
    result = []
    for i in range(2, n):
        if sieve[i]:
            result.append(i)
    return result


def prime_factors(n):
    result = []
    c = 2
    while (n > 1):
        if (n % c == 0):
            result.append(c)
            n = n / c
        else:
            c = c + 1
    return result


def get_gcd1(a, b):
    while b != 0:
        if b > a:
            a, b = b, a
        a -= b
    return a


def get_gcd2(a, b):
    if b > a:
        a, b = b, a
    while b != 0:
        a = a % b
        a, b = b, a
    return a


def get_lcm(a, b):
    return int(a * b / get_gcd2(a, b))
