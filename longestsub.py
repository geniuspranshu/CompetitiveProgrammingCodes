        

def recur(A,i,res,count):
    n = len(A)
    if i+1<n and res<=A[i+1]:
        res = A[i+1]
        count+=1
        print(A[i+1],i+1,"A[i+1]")
        return recur(A,i+1,res,count)
    elif i+1<n and res>A[i+1]:
        return recur(A,i+1,res,count)
    elif (i+1) == n:
#        print(count)
        return count
def recurl(A,i,k,res,count):
    n = len(A)
    if i-1>=k and res>=A[i-1]:
        res = A[i-1]
        count+=1
        print(A[i-1])
        return recurl(A,i-1,res,count)
    elif i-1<n and res<A[i-1]:
        return recur(A,i-1,res,count)
    elif (i-1) == k:
        return count
def longest(A,n):
    count = 0
    maxi = 0
    i=-1;k=0
    while i<n:
        print(i,"i in recursion") 
        maxi = max(recur(A,i,0,count),maxi)
        print("for i = %d max is %d"%(i,maxi))
        i+=1;
    print(maxi)
    #print(recurl(A,n-1,A[n-1],0))
    

arr = [10, 22, 9, 33, 21, 50, 41, 60]
longest(arr,len(arr))

