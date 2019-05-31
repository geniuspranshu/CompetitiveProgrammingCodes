
def longest_increasing_subsequence(arr):

	n = len(arr)
	L = [1]*n

	for i in range(1,n):
		#current position

		for j in range(i):
			#all available previous values
			if arr[i]>arr[j] and L[i]<L[j]+1:
				L[i] = L[j]+1

	return L

def longest_decresing_subsequence(arr):

	n = len(arr)
	L = [1]*n
	#arr = list(reversed(arr))
	print(arr)
	for i in range(n-2,-1,-1):
		#current position

		for j in range(n-1,i-1,-1):
			#all available previous values
			if arr[i]>arr[j] and L[i]<L[j]+1:
				print(arr[i],arr[j])
				L[i] = L[j]+1
	print(L)
	return L
def comabine(arr):

	incre,descre = longest_increasing_subsequence(arr),longest_decresing_subsequence(arr)
	maxi = -99999
	for i in range(len(incre)):
		if maxi<(incre[i]+descre[i]):
			maxi = incre[i]+descre[i]

	print(maxi)




arr = [1,11,2 ,10 ,4 ,5 ,2 ,1]
print("Length of lis is", longest_increasing_subsequence(arr),longest_decresing_subsequence(arr)) 
print("Maximum subsequence is")
comabine(arr)