class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,data):
        t=Node(data)
        if self.head==None:
              self.head=t
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=t
        return self.head 
    def traverse(self):
        curr=self.head
        c=0
        if curr!=None:
            while(curr!=None):
                c+=1
                print(curr.data,"->",end="")
                curr=curr.next
            print("None") 
        print("Count :",c)      
    def reverse(self):
        curr=self.head
        prev=None
        while(curr!=None):
            n=curr.next
            curr.next=prev
            prev=curr
            curr=n 
        self.head=prev
    def middle(self):
        sp=self.head
        fp=self.head
        while(fp.next.next!=None and sp.next!=None):
            sp=sp.next
            fp=fp.next
            fp=fp.next
        print("Middle Element:",sp.data)  
                      
  
li=LinkedList()  
l=list(map(int,input().split()))
for x in l:
    li.insert(x)
li.traverse()
li.reverse()
li.traverse()      
li.middle()
    
          
                        