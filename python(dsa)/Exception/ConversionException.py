s=input()
try:
    c=int(s)
    print(c**2)
    print(c**3)
except ValueError:
    print("Invalid number input")    