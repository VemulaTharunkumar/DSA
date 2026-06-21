l=list(map(int,input().split()))
l.sort()
p1=l[0]*l[1]
p2=l[-1]*l[-2]
print(max(p1,p2))
