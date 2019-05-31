def getnum(x):
	print(x)
	return x[1]

def Schedule(arr):

	n = len(arr)
	arr.sort(key = getnum,reverse=True)
	print(arr)

	visited = [0]*120
	starttime=0
	res = 0
	index = -1
	for i in range(n):

		status = 0
		finish = arr[i][2]
		print("Hello")

		for j in range(arr[i][0],-1,-1):
			print("Hello")
			if finish == 0 and visited[j]==0:
				status = 1
				index=j
				
			elif finish == 0 and visited[j]==1:
				break

			elif visited[j] == 1:
				status = 0
				break
			elif finish>0:
				finish -= 1
				index = j
		if status:
			print(arr[i][1])
			res += arr[i][1] 
			for t in range(j,j+arr[i][2]-1):
				visited[t] = 1

	print(res)





N = 6

Reward = [[1,2,1],[2,3,1],[4,1,2],[10,10,10],[15,13,10],[15,7,5]]
Schedule(Reward)