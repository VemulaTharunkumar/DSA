def strong(n):
	s=0
	while n!=0:
		rem=n%10
		s=s+fact(rem)
		n=n//10
	return s
def fact(n):
	if n==1:
		return 1
	else:
		return n*fact(n-1)

n=int(input())
e=strong(n)
y=lambda v:"Strong" if n==e else "Not Strong Number"
print(y(n))