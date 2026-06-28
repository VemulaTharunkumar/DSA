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
    def delete_last_occurrence(self, x):
        last = None          
        prev_last = None     
        prev = None
        cur = self.head
        while cur:
            if cur.data == x:
                last = cur
                prev_last = prev
            prev = cur
            cur = cur.next
        if last is None:
            return
        if prev_last is None:
            self.head = self.head.next
        else:
            prev_last.next = last.next
    def traversal(self):
        cur = self.head
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")
l1=LinkedList()
arr = list(map(int, input("Enter list elements: ").split()))
for i in arr:
    l1.insert_at_end(i)
l1.traversal()
x = int(input("Enter value to delete: "))
l1.delete_last_occurrence(x)
l1.traversal()
