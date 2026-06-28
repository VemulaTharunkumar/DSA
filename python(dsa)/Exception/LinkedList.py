class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_head(self,x):
        t=Node(x)
        t.next=self.head
        self.head=t
        return self.head
    def insert_at_end(self,x):
        t=Node(x)
        if self.head is None:
            self.head=t
        else:
            cur=self.head
            while cur.next is not None:
                cur=cur.next
            cur.next=t
        return self.head
    def insert_at_pos(self,x,pos):
        t=Node(x)
        if pos<1:
            return self.head
        elif pos==1:
            t1=self.head.next
            self.head.next=t
            t.next=t1
        else:
            cur=self.head
            for i in range(1,pos-1):
                if cur==None:
                    return self.head
                cur=cur.next
            t2=cur.next
            cur.next=t
            t.next=t2
        return self.head
    def delete_head(self):
        if self.head==None:
            return self.head
        else:
            t1=self.head
            self.head=self.head.next
            t1=None
        return self.head
    def delete_at_end(self):
        if self.head==None:
            return None
        elif self.head.next==None:
            self.head=None
            return None
        else:
            cur=self.head
            while cur.next==None:
                prev=cur
                cur=cur.next
            prev.next=None
            cur=None
        return self.head
    def delete_at_pos(self,pos):
        t=self.head
        if pos<=0:
            return None
        elif pos==1:
            self.head=self.head.next
            t=None
            return self.head
        else:
            prev=None
            cur=self.head
            for i in range(1,pos):
                prev=cur
                cur=cur.next
            t1=cur.next
            prev.next=t1
            cur=None
            return self.head
    def traversal(self):
        cur=self.head
        while cur!=None:
            print(cur.data,"->",end="")
            cur=cur.next
        print("none")
    def search(self,x):
        cur=self.head
        while cur!=None:
            if cur.data==x:
                return True
            cur=cur.next
        return False
    def search1(self,x,head):
        if self.head==None:
            return False
        if self.head.data==x:
            return True
        return search1(self,x,head.next)
l = LinkedList()
while True:
    print("\n------ Linked List Menu ------")
    print("1. Insert at Head")
    print("2. Insert at End")
    print("3. Insert at Position")
    print("4. Delete Head")
    print("5. Delete at End")
    print("6. Delete at Position")
    print("7. Traversal")
    print("8. Search")
    print("9. Exit")
    ch = int(input("Enter your choice : "))
    match ch:
        case 1:
            x = int(input("Enter value : "))
            l.insert_at_head(x)
        case 2:
            x = int(input("Enter value : "))
            l.insert_at_end(x)
        case 3:
            x = int(input("Enter value : "))
            pos = int(input("Enter position : "))
            l.insert_at_pos(x, pos)
        case 4:
            l.delete_head()
        case 5:
            l.delete_at_end()
        case 6:
            pos = int(input("Enter position : "))
            l.delete_at_pos(pos)
        case 7:
            l.traversal()
        case 8:
            x = int(input("Enter element to search : "))
            if l.search(x):
                print("Element Found")
            else:
                print("Element Not Found")
        case 9:
            print("Exiting...")
            break
        case _:
            print("Invalid Choice")