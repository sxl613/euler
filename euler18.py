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


def solve_rec(triangle, start_h, start_w):
    """

    :param triangle: 	List of list implementation of the input triangle.
    :param start_h: 	Start heigh.
    :param start_w:		Start width.
    :return: 	The maximum sum possible to obtain by traversing the triangle.
    """
    n = len(triangle)
    # Base case: if the function hits the bottom row, it needs to return the value at the indexed element.
    if start_h == n - 1:
        return triangle[start_h][start_w]
    # Otherwise use recursion
    else:
        return triangle[start_h][start_w] + max(
            solve_rec(triangle, start_h + 1, start_w),
            solve_rec(triangle, start_h + 1, start_w + 1),
        )


def solveTriangle(path: str):
    triangle = []
    with open(path, "r") as f:
        d = f.readlines()
        for line in d:
            triangle.append([int(i) for i in line.split()])
    return solve_rec(triangle, 0, 0)


if __name__ == "__main__":
    path = str(sys.argv[1])
    print(solveTriangle(path))
