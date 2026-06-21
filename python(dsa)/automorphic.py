def automorphic(n):
    sq=n*n
    while n>0:
        if n%10!=sq%10:
            return False
        n//=10
        sq//=10

    return True

n = int(input())

if automorphic(n):
    print(f"{n} is automorphic")
else:
    print(f"{n} is not automorphic")