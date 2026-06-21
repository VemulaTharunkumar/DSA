import heapq

l=[]
heapq.heapify(l)

while True:
	x=int(input())
	match x:
		case 1:
			p=int(input())
			heapq.heappush(l,p)
			print(l)
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
				print("Min element:",l[0])
		case 4:
			exit()