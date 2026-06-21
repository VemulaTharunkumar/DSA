def GCD(x,y):
	if y==0:
		return x
	return GCD(y,x%y)
x,y=map(int,input().split())
u=GCD(x,y)
print(u)
	