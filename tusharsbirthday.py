
maxkick=-99999
def permute(arr,n,level,L,S,kick,steps):
	global maxsteps

	if level == n and kick> maxkick:
		maxsteps = kick
		print(L)

	elif level < n:
		i=0
		while kick<=S:
			
			if kick + i*arr[level] <= S :

				kick += i*arr[level]
				
				L[level] = i*arr[level] 
				permute(arr,n,level+1,L,S,kick,steps+i)
				L[level] -= i*arr[level]
				kick -= i*arr[level]
				i += 1
			else:
				break

R = 12; S = [6,8,5,4,7]
permute(S,5,0,[0]*5,12,0,0)
