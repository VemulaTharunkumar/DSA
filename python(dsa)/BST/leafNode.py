class Node:
    def __init__(self,data):
        self.data=data
        self.l=None
        self.r=None

class BST:
    c=0
    def __init__(self):
        self.root=None

    def insert(self,root,x):
        if root==None:
            return Node(x)

        if x<root.data:
            root.l=self.insert(root.l,x)
        elif x>root.data:
            root.r=self.insert(root.r,x)
        else:
            print("Duplicate..")
            return root

        return root

    def traverse(self,root):
        if root is not None:
            self.traverse(root.l)
            if root.l is None and root.r is None:
                BST.c+=1
            self.traverse(root.r)
    def smallest(self,root):
        if root is None:
            return
        curr=root
        while curr!=None and curr.l!=None:
            curr=curr.l
        print(curr.data) 
        return root          

b=BST()

l=list(map(int,input().split()))

for x in l:
    b.root=b.insert(b.root,x)

b.traverse(b.root)
print(BST.c)
b.root=b.smallest(b.root)