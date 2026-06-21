n=int(input())
l=[]
while n%2==0:
	l.append(2)
	n=n//2

for i in range(3,n,2):
	while n%i==0:
		l.append(i)
		n=n//i
if n>2:
	l.append(n)

s=set(l)
print(s)