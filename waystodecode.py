
def waysto(Arr):

	n = len(Arr)
	if n<2 and Arr[n-1]=='0':
		return 0
	elif n<2:
		return 1
	count = [0] * (n+1)

	count[0] = 1

	if Arr[0] == '0':
		count[1] = 0
	else:
		count[1]=1

	for i in range(2,n+1):

		if Arr[i-1]>'0':
			count[i] = count[i-1]

		if Arr[i-2] == '1' or (Arr[i-2] == '2' and Arr[i-1]<'7'):
			count[i] += count[i-2]
		#print(count)
	return count[n]


Arr = input()

num = waysto(Arr)
print(num)
