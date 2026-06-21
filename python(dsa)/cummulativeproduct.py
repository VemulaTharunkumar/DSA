n=list(map(int,input().split()))
pr=[1]*len(n)
pr[0]=n[0]
for i in range(1,len(n)):
	pr[i]=pr[i-1]*n[i]

print(pr)
