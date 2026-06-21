import math
n=int(input())
li=[]
small=[]
small.append(1)
large=[]
for i in range(2,int(math.sqrt(n))+1):
	if n%i==0:
		small.append(i)
		if n//i!=i:
			large.append(n//i)
li=small+large[::-1]
li.append(n)
print(li)
print("Min ",li[0])
print("Max",li[-1])
