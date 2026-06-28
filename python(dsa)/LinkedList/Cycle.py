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
            while cur.next is not None:
                cur = cur.next
            cur.next = t

    def traversal(self):
        cur = self.head
        while cur is not None:
            print(cur.data, "->", end=" ")
            cur = cur.next
        print("None")
    def create_cycle(self, pos):
        cur = self.head
        target = self.head
        for _ in range(pos):
            target = target.next
        while cur.next:
            cur = cur.next
        cur.next = target
    def has_cycle(self):
        sp=self.head
        fp=self.head
        while fp.next is not None:
            sp=sp.next
            fp=fp.next.next
            if sp==fp:
                print("Cycle detected")
                return True
        return False
    def start_ele(self):
        visited=set()
        cur=self.head
        while cur:
            if cur in visited:
                print("start Element of the cycle :",cur.data)
                return True
            visited.add(cur)
            cur=cur.next
        return False
l=LinkedList()
l1=list(map(int,input().split()))
for i in l1:
    l.insert_at_end(i)
l.create_cycle(2)
print(l.has_cycle())
print(l.start_ele())
