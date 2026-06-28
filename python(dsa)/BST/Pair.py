class Node:
    def __init__(self,data):
        self.data=data
        self.l=None
        self.r=None

class BST:
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
    def traverse(self,root,t):
        if root is not None:
            self.traverse(root.l,t)
            if t-root.data in BST.s:
                print(t-root.data,root.data)
                BST.Found=True
            BST.s.add(root.data)       
            self.traverse(root.r,t)
    def levelOrder(self,root):
        l=[]
        l.append(root)
        while l:
            q=l.pop(0)
            print(q.data,end=" ")
            if q.l is not None:
                l.append(q.l)
            if q.r is not None:
                l.append(q.r)  
        return root 
    def reverselevelOrder(self,root):
        l=[]
        s=[]
        l.append(root)
        while l:
            q=l.pop(0)
            s.append(q)
            if q.r is not None:
                l.append(q.r)
            if q.l is not None:
                l.append(q.l)  
        while s:
            print(s.pop().data,end=" ")        
        return root 
             
            
            
                    
        
b=BST()
l=list(map(int,input().split())) 
for x in l:       
    b.root=b.insert(x) 
b.reverselevelOrder(b.root)      
    

    
    
            
            
                                
                        