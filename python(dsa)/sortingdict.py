k=list(input().split())
v=list(map(int,input().split()))
d=dict(zip(k,v))

while(True):
	x=int(input())
	match x:
		case 1:
			dict1=dict(sorted(d.items()))
			print(dict1)
			dict3=dict(sorted(d.items(),reverse=True))
			print(dict3)
		case 2:
			dict2=dict(sorted(d.items(),key=lambda x:x[1]))
			print(dict2)
			dict4=dict(sorted(d.items(),reverse=True))
			print(dict4)
		case 3:
			exit()
	
