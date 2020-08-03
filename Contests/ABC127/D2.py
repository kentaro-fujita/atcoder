import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))
BC = [list(map(int, input().split())) for _ in range(M)]

heapq.heapify(A)

BC = sorted(BC, key=lambda x: x[1], reverse=True)
for b, c in BC:
    for i in range(b):
        a = heapq.heappop(A)
        if a < c:
            heapq.heappush(A, c)
        else:
            heapq.heappush(A, a)
            break

print(sum(A))
