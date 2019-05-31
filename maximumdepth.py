
class Node(object):
	"""docstring for Node"""
	def __init__(self, val,level=0):
		super(Node, self).__init__()
		self.val = val
		self.level = level
	
		

N,Q = input().split(" ")
N = int(N);Q = int(Q)
L = [[] for j in range(N+1)]
arr = []
arr.append(0)
for i in input().split(" "):

	arr.append(Node(int(i)))
maxdepth = 0
for i in range(N-1):

	u,v = input().split(" ")
	u = int(u);v = int(v)

	a = arr[u]
	b = arr[v]
	b.level = a.level + 1
	if a not in L[a.level]:
		L[a.level].append(a)
	if b not in L[b.level]:
		L[b.level].append(b)
		maxdepth = max(maxdepth,b.level)

for i in range(Q):

	l,x = input().split(" ")
	l = int(l);x = int(x)
	l = l % (maxdepth+1)
	res = 99999999
	for j in L[l]:

		if j.val> x and j.val<res:
			res = j.val
	if res == 99999999:
		print(-1)
	else:
		print(res)

