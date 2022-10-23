def is_palindrome(n):
    n = abs(n)
    if n / 10 < 1:
        return True
    else:
        divisor = 1
        while n / divisor >= 10:
            divisor *= 10

        while n / 10 > 1:
            if n // divisor != n % 10:
                return False
            else:
                n = (n % divisor - n % 10) / 10
                divisor = divisor / 100
        return True

