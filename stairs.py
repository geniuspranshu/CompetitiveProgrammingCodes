
def staris(stair_no):
	n = stair_no
	L = [0]*(n+1) 
	L[1] = 1
	L[2] = 2

	for i in range(3,stair_no+1):
		L[i] = L[i-1]+L[i-2]

	return L[stair_no]


stair_no = int(input())

print("number of ways to reach is = ",staris(stair_no))
