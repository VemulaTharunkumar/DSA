a,b=map(int,input().split())
try:
    print(a+b)
    print(a*b)
    print(a//b)
except ZeroDivisionError:
    print("*Denominator will not be zero*")
    print("Default Value with denominator 2 :",(a//2))
finally:
    print("Program executed")    
    
        
    