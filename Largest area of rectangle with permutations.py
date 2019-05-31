
def maxArea(mat):
	row = len(mat)
	col = len(mat[0])

	L = [[0 for i in range(col)] for j in range(row)]

	for i in range(col):
		L[0][i] = mat[0][i]
		for j in range(1,row):

			if mat[j][i] == 1:

				L[j][i] = L[j-1][i] + 1

	for r in range(row):
		L[r].sort(reverse = True)
	print(L)

	max_area = 0

	for i in range(0, row, 1):
		for j in range(0, col, 1):

			curr_area = (j + 1) * L[i][j] 
			if (curr_area > max_area):
				max_area = curr_area
	return max_area



if __name__ == '__main__': 
    mat = [[0, 1, 0, 1, 0], 
           [0, 1, 0, 1, 1], 
           [1, 1, 0, 1, 0]] 
    print("Area of the largest rectangle is",maxArea(mat)) 