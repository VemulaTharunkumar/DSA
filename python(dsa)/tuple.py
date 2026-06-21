n=list(map(int,input().split()))
t=tuple(n)
print(t)
l1=list(t)
l1.append(50)
t1=tuple(l1)
print(t1)
l2=list(t1)
l1[2]=100
t2=tuple(l1)
print(t2)

