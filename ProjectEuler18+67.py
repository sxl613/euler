"""
	My python solution to Project Euler 18/67. Two implementations, one recursive and one iterative.
	The task is to compute a max path in a triangle where from each point in the triangle you can go down to two adjacent numbers.
	For example, in the triangle below, possible moves from 47 in the 3rd row are 35 and 87. This implementation uses dynamic programming.
	Task 18 input:

								    75
							       95 64
								  17 47 82
								18 35 87 10
							   20 04 82 47 65
							  19 01 23 75 03 34
							 88 02 77 73 07 63 67
							99 65 04 28 06 16 70 92
						   41 41 26 56 83 40 80 70 33
						  41 48 72 33 47 32 37 16 94 29
						53 71 44 65 25 43 91 52 97 51 14
					   70 11 33 28 77 73 17 78 39 68 17 57
					 91 71 52 38 17 14 91 43 58 50 27 29 48
					63 66 04 68 89 53 67 30 73 16 69 87 40 31
				   04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

Task 67's input is a triangle with 100 rows taken from a .txt at the specified path.

"""
def inputTriangle(triangle, n):
	"""

	:param triangle: 	A list containing the numbers to be put in the input triangle.
	:param n: 			Triangle height.
	:return: 			A list of lists implementation of the input triangle.
	"""
	res = []
	for i in range(n):
		res.append([])
		for j in range(i+1):
			(res[i]).append(int(triangle[int(((i)*(i+1))/2) + j]))
	return res

def maxSum_recursive(triangle, n, start_h, start_w):
	"""

	:param triangle: 	List of list implementation of the input triangle.
	:param n: 			Triangle's height.
	:param start_h: 	Start heigh.
	:param start_w:		Start width.
	:return: 	The maximum sum possible to obtain by traversing the triangle.
	"""

	# Base case: if the function hits the bottom row, it needs to return the value at the indexed element.
	if start_h == n - 1:
		return triangle[start_h][start_w]
	# Otherwise use recursion
	else:
		return triangle[start_h][start_w] + max(maxSum_recursive(triangle, n, start_h + 1, start_w), maxSum_recursive(triangle, n, start_h + 1, start_w + 1))


def maxSum_iterative(triangle, n, start_h, start_w):
	"""

	:param triangle: 	List of list implementation of the input triangle.
	:param n: 			Triangle's height.
	:param start_h: 	Start heigh.
	:param start_w:		Start width.
	:return: 	The maximum sum possible to obtain by traversing the triangle.

	This is the iterative version of the algorithm above.
	"""
	stack = [(start_h, start_w)]
	# Implementing a copy of the triangle filled with -1; used for holding intermediate max paths - element at (i, j) holds the maximum path starting at that element
	paths = []
	for i in range(n):
		paths.append([])
		for j in range(i + 1):
			(paths[i]).append(-1)
	######
	while len(stack) > 0:
		(i, j) = stack.pop()
		if i == n - 1:
			paths[i][j] = triangle[i][j]
		else:
			if paths[i+1][j] != -1 and paths[i+1][j+1] != -1:
				paths[i][j] = triangle[i][j] + max(paths[i+1][j], paths[i+1][j+1])
			else:
				stack.append((i, j))
			if paths[i+1][j] == -1:
				stack.append((i+1, j))
			if paths[i+1][j+1] == -1:
				stack.append((i + 1, j+1))
	return paths[0][0]

def solveTriangle(path, n):
	triangle = []
	with open(path, 'r') as f:
		for line in f:
			triangle.append([int(i) for i in line.split()])
	return maxSum_iterative(triangle, n, 0, 0)

if __name__ == '__main__':
	print(solveTriangle(input(), int(input())))

