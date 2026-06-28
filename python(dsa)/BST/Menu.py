class Node:
    def __init__(self,data):
        self.data=data
        self.l=None
        self.r=None

class BST:
    def __init__(self):
        self.root=None

    def insert_itr(self,x):
        t=Node(x)

        if self.root==None:
            self.root=t
            return

        curr=self.root
        prev=None

        while curr!=None:
            prev=curr

            if x<curr.data:
                curr=curr.l
            elif x>curr.data:
                curr=curr.r
            else:
                print("Duplicate Element")
                return

        if x<prev.data:
            prev.l=t
        else:
            prev.r=t

    def insert_rec(self,root,x):
        if root==None:
            return Node(x)

        if x<root.data:
            root.l=self.insert_rec(root.l,x)
        elif x>root.data:
            root.r=self.insert_rec(root.r,x)
        else:
            print("Duplicate Element")

        return root

    def getSuccessor(self,root):
        while root and root.l:
            root=root.l
        return root

    def delete_itr(self,x):
        curr=self.root
        par=None

        while curr!=None and curr.data!=x:
            par=curr

            if x<curr.data:
                curr=curr.l
            else:
                curr=curr.r

        if curr==None:
            print("Element Not Found")
            return

        if curr.l==None and curr.r==None:

            if par==None:
                self.root=None
            elif par.l==curr:
                par.l=None
            else:
                par.r=None

        elif curr.l==None:

            if par==None:
                self.root=curr.r
            elif par.l==curr:
                par.l=curr.r
            else:
                par.r=curr.r

        elif curr.r==None:

            if par==None:
                self.root=curr.l
            elif par.l==curr:
                par.l=curr.l
            else:
                par.r=curr.l

        else:
            succ_par=curr
            succ=curr.r

            while succ.l!=None:
                succ_par=succ
                succ=succ.l

            curr.data=succ.data

            if succ_par.l==succ:
                succ_par.l=succ.r
            else:
                succ_par.r=succ.r

    def delete_rec(self,root,x):

        if root==None:
            return None

        if x<root.data:
            root.l=self.delete_rec(root.l,x)

        elif x>root.data:
            root.r=self.delete_rec(root.r,x)

        else:

            if root.l==None:
                return root.r

            if root.r==None:
                return root.l

            temp=self.getSuccessor(root.r)

            root.data=temp.data

            root.r=self.delete_rec(root.r,temp.data)

        return root


    def traverse(self,root):
        if root!=None:
            self.traverse(root.l)
            print(root.data,end=" ")
            self.traverse(root.r)


b=BST()

while True:

    print("\n1.Insert Iterative")
    print("2.Insert Recursive")
    print("3.Delete Iterative")
    print("4.Delete Recursive")
    print("5.Traverse")
    print("6.Exit")

    ch=int(input("Enter Choice: "))

    if ch==1:
        x=int(input("Enter Element: "))
        b.insert_itr(x)

    elif ch==2:
        x=int(input("Enter Element: "))
        b.root=b.insert_rec(b.root,x)

    elif ch==3:
        x=int(input("Enter Element To Delete: "))
        b.delete_itr(x)

    elif ch==4:
        x=int(input("Enter Element To Delete: "))
        b.root=b.delete_rec(b.root,x)

    elif ch==5:
        if b.root==None:
            print("Tree Empty")
        else:
            b.traverse(b.root)
            print()

    elif ch==6:
        print("Exiting...")
        break

    else:
        print("Invalid Choice")