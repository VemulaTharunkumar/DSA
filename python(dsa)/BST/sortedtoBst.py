class Node:
    def __init__(self,data):
        self.data=data
        self.l=None
        self.r=None

class BST:
    def __init__(self):
        self.root=None

    def sortedToBST(self,a,low,high):
        if low>high:
            return None

        mid=(low+high)//2

        root=Node(a[mid])

        root.l=self.sortedToBST(a,low,mid-1)
        root.r=self.sortedToBST(a,mid+1,high)

        return root

    def inorder(self,root):
        if root:
            self.inorder(root.l)
            print(root.data,end=" ")
            self.inorder(root.r)

b=BST()

a=list(map(int,input().split()))

b.root=b.sortedToBST(a,0,len(a)-1)

b.inorder(b.root)