n=int(input())
l=[]

for i in range(n):
    x=int(input())
    l.append(x)

t1=tuple(l)
print(t1)

l1=sorted(t1)

k=int(input())
if k==0 or k>n:
	print("Invalid k")
	exit()

l2=l1[:k]
l3=l1[-k:]

t3=tuple(l2)
t4=tuple(l3)

print("min k:",t3)
print("max k:",t4)
