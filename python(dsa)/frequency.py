n = int(input())
f = {}

for i in range(n):
    x = int(input())
    f[x] = f.get(x, 0) + 1

print("Output :")

m = max(f.values())

k = float('inf')

for x in f:
    if f[x] == m and x < k:
        k = x

print(k)