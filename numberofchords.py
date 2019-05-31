'''

def ways(num):
	if num%2 !=0:
		return 0
	else:
		

		n = num//2 
		count = [0]*(n+1)
		count[0] = 0
		count[1] = 1
		count[2] = 1
		#count[4] = 2
		if num>2:
			for i in range(2,n+1):
				for j in range(0,i-1):
					print(i,count[j],count[i-j-1])
					count[i] += count[j] * count[i-j-1]

		return count		





chord = int(input())
total = ways(chord)
print(total)
'''
def chordCnt( A):
 
    # n = no of points required
    n = 2 * A
 
    # dp array containing the sum
    dpArray = [0]*(n + 1)
    dpArray[0] = 1
    dpArray[2] = 1
    for i in range(4, n + 1, 2):
        for j in range(0, i-1, 2):
            dpArray[i] += (dpArray[j]*dpArray[i-2-j])
 
    # returning the required number
    return int(dpArray[n])
 
# driver code
N = 3
print(chordCnt( N))
