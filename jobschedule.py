

def Schedule(arr):

	n = len(arr)
	arr.sort()
	print(arr)
	L=[0]*n
	for i in range(n):
		L[i] = arr[i][1]

	for i in range(1,n):
		starttime = 0
		for j in range(i):
			print("i,j",i,j)
			if starttime+arr[j][2] <= abs(arr[i][0]-arr[i][2]):
				print("arr[j] arr[i]",arr[j][1],arr[i][1])
				if L[j] + arr[i][1] > L[i]:
					print("Hel",i,j,L[i],L[j]+arr[i][1])
					L[i] = L[j]+arr[i][1]
					print("L = ",L)
					starttime += arr[i][2]

	print(L)



N = 6

Reward = [[1,2,1],[2,3,1],[4,1,2],[10,10,10],[15,13,10],[15,7,5]]
Schedule(Reward)