l=list(map(int,input().split()))
s=0
for i in range(0,len(l)):
	if i&1==1:
		s+=l[i]
print("Sum of odd indices:",s)