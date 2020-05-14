n = int(input())

s = [0] * (10**6 + 1)
for _ in range(n):
    a, b = map(int, input().split())

    s[a] += 1
    if b + 1 < 10**6 + 1:
        s[b+1] -= 1

ans = s[0]
for i in range(10**6):
    s[i+1] += s[i]
    ans = max(ans, s[i+1])

print(ans)
