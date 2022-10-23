def prefix_function(s):
    result = [0] * len(s)

    for i in range(1, len(s)):
        j = result[i - 1]

        while j > 0 and s[i] != s[j]:
            j = result[j - 1]

        if s[i] == s[j]:
            j += 1
        result[i] = j

    return result


def KMP(base_str, substr):
    p = prefix_function(substr + "#" + base_str)

    for i in range(len(base_str)):
        if p[len(substr) + 1 + i] == len(substr):
            print("s[" + i - len(substr) + 1 + "]")

