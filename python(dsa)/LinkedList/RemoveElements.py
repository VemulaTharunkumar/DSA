class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self, x):
        t = Node(x)
        if self.head is None:
            self.head = t
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = t
    def remove_x(self,x):
        while self.head and self.head.data == x:
            self.head =self.head.next
        cur=self.head
        while cur and cur.next:
            if cur.next.data==x:
                cur.next=cur.next.next
            else:
                cur=cur.next
    def traversal(self):
        cur = self.head
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")
l = LinkedList()
arr = list(map(int, input("Enter elements: ").split()))
for i in arr:
    l.insert_at_end(i)
x = int(input("Enter element to remove: "))
print("Before deletion:")
l.traversal()
l.remove_x(x)
print("After deletion:")
l.traversal()