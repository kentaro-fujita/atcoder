n = int(input())
a = list(map(int, input().split()))

decimal = sum(a) / len(a) - sum(a) // len(a)
if decimal >= 0.5:
    m = sum(a) // len(a) + 1
else:
    m = sum(a) // len(a)

ans = 0
for i in range(n):
    ans += (a[i] - m)**2

print(ans)
