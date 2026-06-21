def enque(x):
	l.append(x)
	print("------------")
	print(l)
def deque():
	x=l[0]
	l.pop(0)
	print("poped :",x)
def front():
	return l[0]
def rear():
	return l[-1]
def isEmpty():
	if len(l)==0:
		return True
	else:
		return False
def size():
	if len(l)==0:
		return 0
	else:
		return len(l)

l=[]
while True:
	print("1.Enque ")
	print("2.Deque ")
	print("3.front ")
	print("4.rear ")
	print("5.isEmpty")
	print("6.Size")
	print("7.exit")
	x=int(input())
	match x:
		case 1:
			a=int(input())
			enque(a)
		case 2:
			deque()
		case 3:
			print("Front element:",front())
		case 4:
			print("Rear:",rear())
		case 5:
			print("isEmpty?",isEmpty())
		case 6:
			print("Size :",size())	
		case 7:
			exit()
		case _:
			print("Enter valid choice")
	