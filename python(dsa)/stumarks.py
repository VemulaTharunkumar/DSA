n=int(input())
d={}
for i in range(n):
	x=input()
	y=int(input())
	d[x]=y

k=input()
print("Score:",d[k])
g=d.values()
s=max(g)
for j in d:
	if d[j]==s:
		print("Student with max score:",j)


	