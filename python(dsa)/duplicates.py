n=list(map(int,input().split()))
res=[]
for x in n:
	if(n.count(x)==1):
		res.append(x)

print(res)