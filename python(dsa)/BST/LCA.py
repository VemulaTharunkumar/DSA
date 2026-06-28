class Node:
    def __init__(self,data):
        self.data=data
        self.l=None
        self.r=None

class BST:
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

    def LCA(self,root,n1,n2):
        if root is None:
            return None
        if n1<root.data and n2<root.data:
            return self.LCA(root.l,n1,n2)
        elif n1>root.data and n2>root.data:
            return self.LCA(root.r,n1,n2)
        return root

b=BST()
l=list(map(int,input().split()))
for x in l:
    b.root=b.insert(x)

n1=int(input("Enter n1: "))
n2=int(input("Enter n2: "))

if b.search(b.root,n1) and b.search(b.root,n2):
    ans=b.LCA(b.root,n1,n2)
    print("LCA:",ans.data)
else:
    print("One or both nodes not present")