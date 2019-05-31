def numberofchord(num):
	n = 2*num
	L = [0]*(n+1)
	L[0]= 1
	L[2]= 1
	
	for i in range(4,n+1,2):

		for j in range(0,i-1,2):
			print(i,j,i-j-2)
			L[i] += L[j]*L[i-j-2] 

	print(L)



io = int(input())
numberofchord(io)