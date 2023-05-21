import typing as _t
import sys


def inputTriangle(triangle: _t.List, n: int):
    """

    :param triangle: 	A list containing the numbers to be put in the input triangle.
    :param n: 			Triangle height.
    :return: 			A list of lists implementation of the input triangle.
    """
    triangle = [[-1 for _ in range(i + 1)] for i in range(n)]
    for i in range(n):
        for j in range(i + 1):
            triangle[i][j] = int(triangle[int(((i) * (i + 1)) / 2) + j])
    return triangle


def solve_iter(triangle: _t.List, start_h: int, start_w: int) -> int:
    """

    :param triangle: 	List of list implementation of the input triangle.
    :param start_h: 	Start heigh.
    :param start_w:		Start width.
    :return: 	The maximum sum possible to obtain by traversing the triangle.

    This is the iterative version of the algorithm above.
    """
    stack = [(start_h, start_w)]
    n = len(triangle)
    # Implementing a copy of the triangle filled with -1; used for holding intermediate max paths
    # element at (i, j) holds the maximum path starting at that element
    paths = [[-1 for _ in range(i + 1)] for i in range(n)]
    while stack:
        (i, j) = stack.pop()
        # last row
        if i == n - 1:
            paths[i][j] = triangle[i][j]
        else:
            if paths[i + 1][j] != -1 and paths[i + 1][j + 1] != -1:
                paths[i][j] = triangle[i][j] + max(paths[i + 1][j], paths[i + 1][j + 1])
            else:
                stack.append((i, j))
            if paths[i + 1][j] == -1:
                stack.append((i + 1, j))
            if paths[i + 1][j + 1] == -1:
                stack.append((i + 1, j + 1))

    return paths[0][0]


def solveTriangle(path: str):
    triangle = []
    with open(path, "r") as f:
        d = f.readlines()
        for line in d:
            triangle.append([int(i) for i in line.split()])
    return solve_iter(triangle, 0, 0)


if __name__ == "__main__":
    path = str(sys.argv[1])
    print(solveTriangle(path))
