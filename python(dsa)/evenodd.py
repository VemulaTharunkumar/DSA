n=int(input())
li=[]
for i in range(n):
	x=int(input())
	li.append(x)

even=0
odd=0
for i in li:
	if i&1==0:
		even=even+1
	else:
		odd=odd+1

print("Count of evens:",even)
print("Count of odd:",odd)
