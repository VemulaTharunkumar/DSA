n=int(input())
l=[]
for i in range(n):
    t=tuple(map(int,input().split()))
    l.append(t)
k=int(input())
res=[]
for t in l:
    if all(x%k==0 for x in t):
        res.append(t)
print(res)