n=list(map(int,input().split()))
csum=[0]*len(n)
csum[0]=n[0]
for i in range(1,len(n)):
	csum[i]=csum[i-1]+n[i]
print(csum)
	

