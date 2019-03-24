from math import ceil

def it(S, n):
    i = 0
    s = len(S)
    while i < s:
        if S[i] != -1:
            n -= 1
            if n == 0:
                return i
        i += 1
                
def fact(n):
    if n <= 1:
        return 1
    i = n - 1
    while i > 0:
        n *= i
        i -= 1
    return n
    
def f(s, n):
    S = list(range(s))
    res = ''
    i = s - 1
    while i >= 0:
        d = ceil(n / fact(i))
        di = it(S, d)
        n -= (d-1) * fact(i)
        res += str(S[di])
        S[di] = -1
        i -= 1
    return res
        
print('1000000th lexicographic permutation of digits 0123456789 is {}'.format(f(10, 1000000)))     