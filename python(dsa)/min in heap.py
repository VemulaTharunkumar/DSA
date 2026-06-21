import heapq

n = list(map(int, input().split()))
heapq.heapify(n)

print("Ascending:")
while n:
    print(heapq.heappop(n), end=" ")