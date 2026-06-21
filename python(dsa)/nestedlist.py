l=[]
n=int(input("Enter no.of lists: "))
for i in range(n):
    l1=list(map(str,input().split()))
    l.append(l1)
print("1 sort by emp id")
print("2 sort by emp name")
print("3 sort by emp job")
print("4 sort by emp salary")
print("5 sort by location")
print("6 sort by grade")
print("7 exit")
while True:
    c=int(input())
    match c:
        case 1:
            l.sort(key=lambda x : x[0])
            print(l)
        case 2:
            l.sort(key=lambda x : x[1])
            print(l)
        case 3:
            l.sort(key=lambda x : x[2])
            print(l)
        case 4:
            l.sort(key=lambda x : x[3])
            print(l)
        case 5:
            l.sort(key=lambda x: x[4])
            print(l)
        case 6:
            l.sort(key=lambda x: x[5])
            print(l)
        case 7:
            break
        case _:
            print("Invalid choice")