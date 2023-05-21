import typing as _t

def load(path: str = "p081_matrix.txt"):
    with open(path, "r") as f:
        fx = f.readlines()
        M = [[int(i) for i in l.split(",")] for l in fx]
    return M

def f81(M: _t.List):
    # m - number of rows
    # n - number of cols
    m, n = len(M), len(M[0])
    MAX = int(1e15)
    ans = 0
    C = [[0 for _ in M[0]] for _ in M]

    def val(A, x, y):
        if x < 0 or x >= n or y < 0 or y >= m:
            return 1e15
        return A[x][y]

    C[0][0] = M[0][0]
    ans = M[0][0]
    for i in range(1, m):
        ans += M[i][0]
        C[i][0] += ans

    ans = M[0][0]
    for i in range(1, n):
        ans += M[0][i]
        C[0][i] += ans

    for i in range(1, m):
        for j in range(1, n):
            if i == 0 and j == 0:
                continue
            v = min(val(C, i-1, j), val(C, i, j-1))
            C[i][j] = val(M, i, j) + v

    return C[n-1][m-1]

if __name__ == "__main__":
    M = load()
    print(f"Least sum path: {f81(M)}")
