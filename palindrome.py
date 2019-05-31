class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # @param A : head node of linked list
    # @return an integer
    
    def lPalin(self, A):
        #print(A.val)
        lis=[]
        res = 0
        lis1 = self.trav(lis,A)
        print(lis1)
        res = self.pali(lis1,A)
        print(res)
        #return res
    def pali(self,lis1,A):
        
        if lis1:
            print(A.val,lis1)
            if A.val == lis1.pop():
                self.pali(lis1,A.next)
            else:
                return 0
                print("Hello",A.val)
                return(0)
        
        return 1
            
    
    def trav(self,lis,A):
        if A.next:
            #print(A.val)
            lis.append(A.val)
            self.trav(lis,A.next)
        else:
            #print(A.val)
            lis.append(A.val)
            
        #print(lis)
        return lis


node1 = Node(1) 
node2 = Node(1) 
node3 = Node(6)
node4 = Node(4)
node5 = Node(1) 
node1.next = node2 # 12->99
node2.next = node3
node3.next = node4
node4.next = node5
g = Solution()
print(g.lPalin(node1))