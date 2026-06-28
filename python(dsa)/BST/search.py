import heapq
class Node:
    def __init__(self,data):
        self.data=data
        self.l=None
        self.r=None

class BST:
    k=[]
    s=set()
    Found=False
    def __init__(self):
        self.root=None
    def insert(self,x):
        t=Node(x)
        if self.root==None:
            self.root=t
            return self.root
        curr=self.root
        par=None
        while curr!=None:
            par=curr
            if x<curr.data:
                curr=curr.l
            elif x>curr.data:
                curr=curr.r
            else:
                print("Duplicate")  
                return self.root     
        if x<par.data:
            par.l=t
        else:
            par.r=t
        return self.root
    def search(self,root,t):
        if root is None:
            return False
        if t==root.data:
            return True
        elif t<root.data:
            return self.search(root.l,t)
        else:
            return self.search(root.r,t)          
b=BST()
l=list(map(int,input().split())) 
for x in l:       
    b.root=b.insert(x) 
t=int(input())    
b.search(b.root,t) 
               
            