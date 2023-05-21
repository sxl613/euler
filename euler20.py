def f(n):
    """
    Calculates the sum of digits of n!

    Args:
        n: integer
    """
    D = [0] * 100000
    D[0] = 1
    c = 0
    f = 0
    l = 0
    for i in range(2, n + 1):
        c = 0
        for k in range(f, l + 1):
            c = i * D[k] + c
            D[k] = c % 100000
            if k == f and c % 100000 == 0:
                f += 1
            c = c // 100000
        if c > 0:
            l += 1
            D[l] = c
    return sum(
        [
            (
                (i % 10)
                + ((i // 10) % 10)
                + ((i // 100) % 10)
                + ((i // 1000) % 10)
                + ((i // 10000) % 10)
                + ((i // 100000) % 10)
            )
            for i in D[f : l + 1]
        ]
    )


if __name__ == "__main__":
    print(f"Sum: {f(100)}")
