
def longestpalin(st):
	n = len(st)
	table = [[0 for i in range(n)] for j in range(n)]
	print(len(table),len(table[0]))
	strat = 0
	maxlen = 0
	for i in range(n):
		table[i][i] = 1
	for i in range(n-1):
		if st[i] == st[i+1]:
			start = i
			maxlen = 2
			table[i][i+1] = 1

	k = 3
	for k in range(3,n+1):
		i=0
		while i<(n-k+1):

			j = i + k -1
			print(i,j)
			print("i+1,j-1",i+1,j-1)	
			if table[i+1][j-1] and st[i] == st[j]:
				table[i][j] = 1

				if k > maxlen:
					start = i 
					maxlen = k
			i+=1

	print(start,maxlen)
	#print(table)


st = "pranshuuhsnarp"
l = longestpalin(st)
