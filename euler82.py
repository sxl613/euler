import typing as _t

def load(path: str = "p082_matrix.txt"):
    with open(path, "r") as f:
        fx = f.readlines()
        M = [[int(i) for i in l.split(",")] for l in fx]
    return M

def f82(M: _t.List):
    # m - number of rows
    # n - number of cols
    m, n = len(M), len(M[0])
    MAX = int(1e15)
    C = [[0 for _ in M[0]] for _ in M]
    R = [[MAX for _ in M[0]] for _ in M]
    # inititalize first columns of C and R
    for i in range(m):
        C[i][0] = M[i][0]
        R[i][0] = M[i][0]

    # initiliaze prefix sum of columns
    ans = M[0][0]
    for i in range(1, n - 1): 
        ans = 0
        for j in range(m):
            ans += M[j][i]
            C[j][i] = ans

    for i in range(1, n-1):
        for j in range(m):
            # entry at row k
            for k in range(m-1, j-1, -1):
                _v = C[j-1][i] if j-1 >= 0 else 0
                v = R[k][i-1] + C[k][i] - _v
                R[j][i] = min(R[j][i], v)
            for u in range(j):
                v = (C[j][i] - C[u][i]) + R[u][i]
                R[j][i] = min(R[j][i], v)
    return min(R[r][-2] + M[r][-1] for r in range(m))


if __name__ == "__main__":
    M = load()
    print(f"Least sum path: {f82(M)}")
