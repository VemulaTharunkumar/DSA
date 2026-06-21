import calci,NumberOperator
def calci1(a,b):
    r=calci.add(a,b)
    print("Add :",r)
    s=calci.multiply(a,b)
    print("Multiply:",s)
    t=calci.i_division(a,b)
    print("iDivision :",t)
    u=calci.f_division(a,b)
    print("fDivision :",u)
    v=calci.m_division(a,b)
    print("mDivision :",v)
    
def no(x):
    q=NumberOperator.double(x)
    print("Double :",q)
    r=NumberOperator.half(x)
    print("Half :",r)
    s=NumberOperator.square(x)
    print("Square :",s)
    t=NumberOperator.cube(x)
    print("Cube :",t)    
while True:
    print("1.Calculator")
    print("2.Number Operators")
    x=int(input("Enter choice :"))
    match x:
        case 1:
            x,y=map(int,input().split())
            calci1(x,y)
        case 2:
            c=int(input())
            no(c)
        case 3:
            exit()
        case _:
            print("Invalid choice")            
