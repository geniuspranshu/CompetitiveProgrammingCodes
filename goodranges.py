

N,M = input().split(" ")
N = int(N);M = int(M)
L = []
print(L)
left = 1;right = N
for i in range(M):

	a = int(input())
	if a not in L:
		L.append(a)
	L.sort()
	prev = None
	preprev = 1
	sum1 = 1 
	for j in range(len(L)):

		if j == 0:
			prev = L[j]
		elif prev != None:
			print(sum1,L[j],prev)
			sum1 += L[j] -1 + prev + 1 
			prev = L[j]


	sum1 += N
	print(sum1)  




