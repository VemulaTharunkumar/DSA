import math

def prime(l):
    if l < 2:
        return False
    s = int(math.sqrt(l))
    for i in range(2, s + 1):
        if l % i == 0:
            return False
    return True

n = int(input())
li = []

for i in range(1, n + 1):
    if prime(i):
        li.append(i)

print(li)