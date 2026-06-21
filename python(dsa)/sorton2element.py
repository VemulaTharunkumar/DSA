n=int(input())
l=[]
for i in range(n):
    t=tuple(map(int,input().split()))
    l.append(t)
res=sorted(l,key=lambda t:t[1])
print(res)