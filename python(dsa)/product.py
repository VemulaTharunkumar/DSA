n=list(map(int,input().split()))
p=1
for i in range(len(n)):
	p=p*n[i]
print("Product:",p)