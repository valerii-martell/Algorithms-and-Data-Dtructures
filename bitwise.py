def is_two_pow(n):
    return not n & (n - 1)


def is_odd(n):
    return n & 1


def is_even(n):
    return not is_odd(n)


def adder(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a


def subtractor(a, b):
    flag = True
    if a < b:
        flag = False
        a, b = b, a
    while b != 0:
        borrow = ~a & b
        a = a ^ b
        b = borrow << 1
    return a if flag else -a


# russian peasant
# multiplier * multiplicand = multiplier*2 * multiplicant/2 + multiplier if odd
def multiplicator(a, b):
    result = 0
    sign = signum(a) ^ signum(b)
    a, b = abs(a), abs(b)
    while b > 0:
        if b & 1:
            result += a
        a = a << 1
        b = b >> 1
    return result if not sign else -result


#
def divider(dividend, divisor):
    sign = signum(dividend) ^ signum(divisor)
    dividend, divisor = abs(dividend), abs(divisor)
    quotient = 0
    temp = 0

    for i in range(31, -1, -1):
        #print("---------------iteration{}-------------".format(i))
        #print("temp", temp)
        #print("temp+div<<i", temp + (divisor << i))
        if temp + (divisor << i) <= dividend:
            temp += divisor << i
            quotient |= 1 << i
            #print("q", quotient)

    return quotient if not sign else -quotient


def pow(a, b):
    result = 1
    while b > 0:
        if b & 1:
            result = result * a
        a = a * a
        b = b >> 1

    return result


def is_zero(n):
    return not bool(adder(n >> 31, -n >> 31))


def signum(n):
    return (n >> 31) - (-n >> 31)


def get_occurrences(arr):
    result = 0
    for i in arr:
        result ^= i
    return result


def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b
