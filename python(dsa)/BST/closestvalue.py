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

    def closest(self,root,x):
        if root is None:
            return None

        ans=root.data

        while root is not None:
            if abs(root.data-x)<abs(ans-x):
                ans=root.data

            if x<root.data:
                root=root.l
            elif x>root.data:
                root=root.r
            else:
                return root.data

        return ans

b=BST()

l=list(map(int,input("Enter elements: ").split()))

for x in l:
    b.root=b.insert(x)

x=int(input("Enter target value: "))

print("Closest value:",b.closest(b.root,x))