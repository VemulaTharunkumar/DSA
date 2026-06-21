def palindrome(n):
	j=len(n)-1
	i=0
	while i<j:
		if n[i]!=n[j]:
			return "Not a palindrome"
		else:
			i=i+1
			j=j-1
	return "palindrome"

n=list(map(int,input().split()))
print(palindrome(n))


	
	
	