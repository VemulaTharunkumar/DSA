class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
class LL:
    c=0
    def __init__(self):
        self.head=None
    def insert_pos(self,x,pos):
        t=Node(x)
        if pos==0:
            t.next=self.head
            self.head=t
        else:
            curr=self.head
            for i in range(pos-1):
                if curr==None:
                    return self.head
                curr=curr.next
            if curr==None:
                return self.head
            t1=curr.next
            curr.next=t
            t.next=t1
        return self.head
    def insert(self,x):
        t=Node(x)
        if self.head==None:
            self.head=t
        else:
            curr=self.head
            while(curr.next!=None):
                curr=curr.next
            curr.next=t
        return self.head        
    def traverse(self):
        curr=self.head
        LL.c=0
        if curr!=None:
            while(curr!=None):
                LL.c+=1
                print(curr.data,"->",end="")
                curr=curr.next
            print("None") 
    def delete_pos(self,n):
        if n==0:
            return None
        else:
            curr=self.head
            prev=None
            for i in range(1,n):
                prev=curr
                if curr==None:
                    return None
                curr=curr.next
                n=curr.next
                if curr==None:
                    return None
            curr=None    
            prev.next=n
        return self.head 
    def findNth(self,n):
        curr=self.head
        curr1=self.head
        for i in range(1,n):
            curr=curr.next
        print(curr.data)    
        for i in range(1,LL.c-n+1):
             curr1=curr1.next  
        print(curr1.data)           
             
li=LL()  
l=list(map(int,input().split()))
for x in l:
    li.insert(x)  
li.traverse()    
n=int(input())
li.delete_pos(n)
li.traverse()

             
                    
                         