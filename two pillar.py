global final
from collections import defaultdict
def twopillars(arr,sum1,sum2,set1,set2,cost):
	global final
	print(set1,set2)
	if sum1 == sum2 and sum1!=0 and sum2 !=0:
		final = sum1
		#print(final)
		return final
	if arr:
		#print(arr,arr[-1],sum1,sum2,set1,set2)
		if cost[sum1][sum2] != None:
			print("Hello")
			return cost[sum1][sum2]
		p = arr.pop(0)
		#print(p)
		a = twopillars(arr[:],sum1+p,sum2,set1+[p],set2,cost)
		b = twopillars(arr[:],sum1,sum2+p,set1,set2+[p],cost)
		c = twopillars(arr[:],sum1,sum2,set1,set2,cost)
		print(a,b,c)
		cost[sum1][sum2] = max(a,b,c)
		cost[sum2][sum1] = max(a,b,c)
		return max(a,b,c)
	else:
		cost[sum1][sum2] = -1
		cost[sum2][sum1] = -1
		return -1

set1=[];set2=[]
arr = [1,2,3,4,6,10]
n = sum(arr)
cost = [[None for i in range(n+1)] for j in range(n+1)]
pillar = twopillars(arr,0,0,set1,set2,cost)
print(pillar)
