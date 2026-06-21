try:
    a,b=map(int,input().split())
    print(a//b)
except ValueError: 
    print("Both inputs must be integer")
except ZeroDivisionError:
    print("Division not posssible")    
       