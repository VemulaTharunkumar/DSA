import heapq

l=[]
heapq._heapify_max(l)

while True:
	x=int(input())
	match x:
		case 1:
			p=int(input())
			heapq.heappush(l,p)
		case 2:
			if(len(l)==0):
				print("Heap empty")
			else:
				heapq.heappop(l)
				print("Element removed")
		case 3:
			if(len(l)==0):
				print("Heap is empty")
			else:
				print("Max element:",l[0])
		case 4:
			print([-p for n in l])
		case 5:
			exit()