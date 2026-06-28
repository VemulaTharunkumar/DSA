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
    def is_palindrome(self):
        stack=[]
        sp=self.head
        fp=self.head
        while fp and fp.next:
            stack.append(sp.data)
            sp=sp.next
            fp=fp.next.next
        if fp:
            sp=sp.next
        while sp:
            if stack.pop()!=sp.data:
                return False
            sp=sp.next
        return True
l = LinkedList()
arr = list(map(int, input().split()))
for i in arr:
    l.insert_at_end(i)
print(l.is_palindrome())
