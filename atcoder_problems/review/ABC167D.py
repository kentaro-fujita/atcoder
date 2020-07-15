n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))

seen = [False] * (n+1)
visited = []
nxt = 1
cnt = 0
while not seen[nxt] and cnt != k:
    seen[nxt] = True
    visited.append(nxt)
    nxt = a[nxt]
    cnt += 1

if cnt == k:
    print(nxt)
    exit()

idx = visited.index(nxt)
print(visited[idx:][(k-idx) % (len(visited)-idx)])
