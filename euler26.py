def f(n):
    """
    Return decimal expansion of 1/n
    """
    S = set()
    k = 10
    res = '0.'
    while k < n:
        res += '0'
        k *= 10
    while k != 0:
        if k < n:
            k *= 10
            res += '0'
        else:
            if k in S:
                return res
            S.add(k)
            t = k // n
            res += str(t)
            k -= t*n
            k *= 10
    return res

L = []
m = 0
m_i = -1
for i in range(1, 1000):
    L.append(len(f(i)[2:]))
    if L[-1] > m:
        m = L[-1]
        m_i = i

print('Max length decimal expansion of 1/n: 1/{}'.format(m_i))