
def minjump(A):

	n = len(A)

	L = [9999999]*n
	L[0] = 0
	for i in range(n):

		m = A[i]

		for j in range(min(i+m,n-1),i,-1):

			L[j] = min(L[j],L[i]+1)
	if L[n-1] == 9999999:

		return -1
	else:
		return L[n-1]



A = [2,3,1,1,4]
print(minjump(A))