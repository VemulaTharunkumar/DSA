class UnderFlow(Exception):
    pass
def push(x):
	l.append(x)
	print("------------")
	print(l)
def pop():
    try:
        if len(l)==0:
            raise UnderFlow
        else:
            x=l[-1]
            l.pop()
            print("poped :",x)
    except UnderFlow:
        print("--Stack is empty pop not possible--")
def top():
    try:
        return l[-1]
    except IndexError:
        print("Stack is empty")
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
	print("1.Push ")
	print("2.POP ")
	print("3.top ")
	print("4.isEmpty ")
	print("5.size")
	print("6.exit")
	x=int(input())
	match x:
		case 1:
			a=int(input())
			push(a)
		case 2:
			pop()
		case 3:
			print("Top element:",top())
		case 4:
			print("isEmpty?:",isEmpty())
		case 5:
			print("Size :",size())	
		case 6:
			exit()
		case _:
			print("Enter valid choice")
	