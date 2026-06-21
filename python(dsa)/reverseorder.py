n=int(input())
l1=[]

for i in range(n):
    x=input()
    l1.append(x)

m=int(input())
l2=[]

for i in range(m):
    x=input()
    l2.append(x)

print("List1 in original order:")
for i in l1:
    print(i)

print("List2 in reverse order:")
for i in range(len(l2)-1,-1,-1):
    print(l2[i])