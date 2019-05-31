
def tushar(W,V,n):

	index1 = V.index(min(V))
	L = [index1]*(W//V[index1])
	kicks = V[index1]*(W//V[index1])
	for i in range(index1+1):

		for j in range(len(L)):

			if L[j]>i and (kicks-V[L[j]] + V[i]) <= W:
				kicks = kicks -V[L[j]] + V[i]

				L[j] = i

	print(L)

W = 12
V = [6,8,5,4,7]
tushar(W,V,5)