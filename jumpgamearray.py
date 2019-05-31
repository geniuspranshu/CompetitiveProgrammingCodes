
def jumpgame(A):
	
	n = len(A)

	L = [0]*n
	L[0] = 1

	for i in range(n):

		if L[i] == 1:

			m = A[i]
			print("i,m",i,m,min(i+m,n-1))
			for j in range(min(i+m,n-1),i,-1):
				print("i = j =",i,j)
				L[j] = 1 

		if L[n-1] == 1:
			return 1
	return 0

A = [3,2,1,0,4]

print(jumpgame(A))


