import math
def perfect(n):
	if n==1:
		return 0
	l=int(math.sqrt(n))
	s=1
	for i in range(2,l+1):
		if n%i==0:
			s=s+i
			if i!=n//i:
				s=s+n//i
	return s

n=int(input())
d=perfect(n)
if n==d:
	print("Perfect Number")
else:
	print("Not a Perfect Number")
		
			