CHAIN = dict()

def chains(n):
    if n < 2:
        return 0
    if n in CHAIN:
        return CHAIN[n]
    else:
        if n % 2 == 0:
            CHAIN[n] = chains(n/2) + 1
        else:
            CHAIN[n] = chains((3*n+1)/2) + 2
    return CHAIN[n]

def longest_chain(N):
    I = 0
    bestI = 0
    for i in range(1, N+1):
        c = chains(i)
        if c > bestI:
            I = i
            bestI = c
    
    return (I, bestI)



print(longest_chain(1000000))