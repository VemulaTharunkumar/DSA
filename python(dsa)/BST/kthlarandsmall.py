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
    def traverse(self,root,p):
        if root is not None:
            self.traverse(root.l,p)
            BST.k.append(root.data)
            self.traverse(root.r,p)            
b = BST()
l = list(map(int, input().split()))
for x in l:
    b.root = b.insert(x)
k = int(input("Enter k :"))
b.traverse(b.root, k)
l = BST.k.copy()
heapq.heapify(BST.k)
for _ in range(k):
    i = heapq.heappop(BST.k)
print("Kth smallest :", i)
p = [-x for x in l]
heapq.heapify(p)
for _ in range(k):
    j = -heapq.heappop(p)
print("Kth largest :", j)
               
            