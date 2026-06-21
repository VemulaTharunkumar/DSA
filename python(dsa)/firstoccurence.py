l=list(map(int,input().split()))
x=int(input())
n=-1
for i in range(0,len(l)):
	if l[i]==x:
		n=i
		break

print(n)
