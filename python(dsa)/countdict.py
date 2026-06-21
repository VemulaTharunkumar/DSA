n=int(input())
f={}
for i in range(n):
	x=int(input())
	f[x]=f.get(x,0)+1;
print("Output :")
c=0
k=int(input("Enter k value :"))
for x in f:
	if f.get(x)==k:
		c+=1
print(c)