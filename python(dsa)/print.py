def printn(n):
	if n==1:
		return 1
	return printn(n-1)

n=int(input())
printn(n)
	