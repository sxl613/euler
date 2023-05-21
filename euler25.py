M = {0 : 1, 1 : 1}
def fib(n, M = {}):
    if n <= 1:
        return 1
    if n in M:
        return M[n]
    M[n] = fib(n - 1) + fib(n - 2)
    return M[n]

def solve():
    i = 0
    while True:
        if math.log10(fib(i, M)) > 999:
            break
        i += 1
    print('Fibonacci number exceeds 1000 digits for n = {}'.format(i))

solve()