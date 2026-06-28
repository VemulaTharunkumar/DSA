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

        if self.root is None:
            self.root=t
            return self.root

        curr=self.root
        par=None

        while curr is not None:
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

    def floor(self,root,x):
        ans=None

        while root is not None:
            if root.data==x:
                return root.data

            if root.data>x:
                root=root.l
            else:
                ans=root.data
                root=root.r

        return ans

    def ceil(self,root,x):
        ans=None

        while root is not None:
            if root.data==x:
                return root.data

            if root.data<x:
                root=root.r
            else:
                ans=root.data
                root=root.l

        return ans

b=BST()

l=list(map(int,input("Enter elements: ").split()))

for x in l:
    b.root=b.insert(x)

x=int(input("Enter value: "))

print("Floor :",b.floor(b.root,x))
print("Ceil :",b.ceil(b.root,x))