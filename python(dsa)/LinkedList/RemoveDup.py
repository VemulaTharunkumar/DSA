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
    def remove_duplicates(self):
        cur=self.head
        while cur and cur.next:
            if cur.data==cur.next.data:
                cur.next=cur.next.next
            else:
                cur =cur.next
    def traversal(self):
        cur = self.head
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")
l=LinkedList()
l1 = list(map(int, input("Enter sorted elements: ").split()))
for i in l1:
    l.insert_at_end(i)
print("Before removing duplicates:")
l.traversal()
l.remove_duplicates()
print("After removing duplicates:")
l.traversal()