import math


def rabbit_moves(stairs_number, max_jump):
    moves = [0] * (stairs_number+1)
    moves[0] = 1

    for i in range(1, stairs_number+1):
        start = max(0, i-max_jump)
        for j in range(start, i):
            moves[i] += moves[j]

    return moves[stairs_number]


def coins(denominations, n):
    result = [0 for _ in range(n+1)]
    result[0] = 1

    for i in range(len(denominations)):
        for j in range(denominations[i], n+1):
            result[j] += result[j-denominations[i]]

    return result[n]


def best_change(denominations, n):
    result = []
    denominations.sort()
    while n > 0:
        if len(denominations) > 0:
            coin = denominations.pop()
        else:
            return None
        if n < coin:
            continue
        while n >= coin:
            n = n // coin if n != coin else 0
            result.append(coin)
        if n == 0:
            return result
    return None


def update_string(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    dp = [[0 for i in range(len1 + 1)]
          for j in range(2)];

    # Base condition when second String
    # is empty then we remove all characters
    for i in range(0, len1 + 1):
        dp[0][i] = i

    # Start filling the DP
    # This loop run for every
    # character in second String
    for i in range(1, len2 + 1):

        # This loop compares the char from
        # second String with first String
        # characters
        for j in range(0, len1 + 1):

            # If first String is empty then
            # we have to perform add character
            # operation to get second String
            if j == 0:
                dp[i % 2][j] = i

            # If character from both String
            # is same then we do not perform any
            # operation . here i % 2 is for bound
            # the row number.
            elif str1[j - 1] == str2[i - 1]:
                dp[i % 2][j] = dp[(i - 1) % 2][j - 1]

            # If character from both String is
            # not same then we take the minimum
            # from three specified operation
            else:
                dp[i % 2][j] = (1 + min(dp[(i - 1) % 2][j],
                                    min(dp[i % 2][j - 1],
                                        dp[(i - 1) % 2][j - 1])))


        return dp[len2 % 2][len1]

def update_string2(str1, str2):

    m = len(str1)
    n = len(str2)

    # Create a table to store results of subproblems
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # Fill d[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):

            # If first string is empty, only option is to
            # insert all characters of second string
            if i == 0:
                dp[i][j] = j  # Min. operations = j

            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                dp[i][j] = i  # Min. operations = i

            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],  # Insert
                                   dp[i - 1][j],  # Remove
                                   dp[i - 1][j - 1])  # Replace

    return dp[m][n]


def combinations(n):
    result = []

    result.append([n])
    def _combinations(n, result):
        result.append([n - 1, 1])
        _combinations(n-1, )

    arr = [1]*n

    for i in range(1, -1):

        result.append([n])
        result.append([n-1, 1])
        combinations()
        pass

    return result


def number_of_all_combos(number):
    if number <= 1:
        return 1
    else:
        res = 0
        for i in range(1, number+1):
            res += number_of_all_combos(number-i)
        return res


# def all_combos(number):
#     result = []
#
#     def _all_combos(number, prefix=[]):
#         if number == 1:
#             result.append(prefix + [1])
#         else:
#             result.append(prefix+[number])
#             for i in range(1, number):
#                 _all_combos(number-i, prefix + [i])
#
#     _all_combos(number)
#     return result


# def all_combos(number, prefix=[]):
#     if number == 1:
#         return [prefix + [1]]
#     else:
#         result = []
#         result.append([prefix + [number]])
#         for i in range(1, number):
#             result += all_combos(number-i, prefix + [i])
#         return result


def all_combos(number, prefix=[]):
    if number == 0:
        return [prefix]
    else:
        result = []
        for i in range(1, number+1):
            result += all_combos(number-i, prefix + [i])
        return result


def number_of_unique_combos(number, max=None):
    if not max:
        max = number
    if number <= 1:
        return 1
    else:
        res = 0
        for i in range(1, min(number, max) + 1):
            res += number_of_unique_combos(number - i, i)
        return res


def all_unique_combos(number, prefix=[], max=None):
    if not max:
        max = number
    if number == 0:
        return [prefix]
    else:
        result = []
        for i in range(1, min(max,number)+1):
            result += all_unique_combos(number-i, prefix + [i], i)
        return result


def all_combos_from_list(lst):
    # lst.sort()
    result = set()

    def _all_combos_from_list(lst):
        if len(lst) > 1:
            result.add(tuple(lst))
            _all_combos_from_list(lst[0:-1])
            _all_combos_from_list(lst[1:])
        else:
            result.add((lst[0],))

    _all_combos_from_list(lst)

    return result


def permutations(lst, prefix=[]):
    if len(lst) == 1:
        return prefix + lst
    else:
        result = []
        for i in range(len(lst)):
            result.append(permutations(lst[:i]+lst[i+1:], prefix+[lst[i]]))
        return result


def unique_prime_combos(s, prime_range=1000):

    def _sieve(prime_range):
        sieve = [True for _ in range(prime_range + 1)]
        sieve[0], sieve[1] = False, False

        for i in range(2, math.floor(math.sqrt(prime_range))):
            if sieve[i]:
                for j in range(i**2, prime_range+1, i):
                    sieve[j] = False

        result = []
        for i in range(prime_range, 2, -1):
            if sieve[i]:
                result.append(i)

        return result

    def _all_unique_prime_combos(s, primes, prefix=[]):

        if len(s) == 0:
            return prefix
        else:
            result = []
            for prime in primes:
                if str(prime) in s[0:len(str(prime))]:
                    # head = s[0:len(str(prime))]
                    tail = s[len(str(prime)):len(s)]
                    if len(tail) == 0:
                        result.append(prefix + [prime])
                    else:
                        result += _all_unique_prime_combos(tail, primes, prefix + [prime])
            return result

    return _all_unique_prime_combos(s, _sieve(prime_range))
