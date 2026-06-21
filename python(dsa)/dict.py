n=int(input())
d={}
for i in range(n):
	x,y=input().split()
	d[x]=y

x=input()
try:
	print("Capital:",d[x])
except KeyError:
	print("Key Not found in dictionary")