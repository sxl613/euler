import time
R = dict()
R[1] = 2
def route(n):
    if n in R:
        return R[n]
    else:
        R[n] = (2*n*(2*n - 1))/n**2 * route(n-1)
    return R[n]

start = time.time()
n = route(130)
elapsed = (time.time() - start)
print("%s found in %.10f seconds" % (n,elapsed))