from functools import reduce

def triangular(n):
    res = 0
    for i in range(n+1):
        res += i
    return res


def prime_factorization(n):
    res = {}
    i = 2
    while i < n+1:
        if n == 1:
            return res
        if n % i == 0:
            n = n / i
            if i in res.keys():
                res[i] += 1
            else:
                res[i] = 1
            i = 1
        i += 1
    return res


def count_factors(n):
    d = prime_factorization(n).values()
    d = [i+1 for i in d]
    return reduce(lambda x, y: x*y, d)

