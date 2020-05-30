n = int(input())
a = list(map(int, input().split()))

if sum(a) % n != 0:
    print(-1)
    exit()

ans = 0
t = sum(a) // n
for i in range(n-1):
    if sum(a[:i+1]) != t * (i+1):
        ans += 1

print(ans)
