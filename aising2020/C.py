n = int(input())

ans = [0] * (n+1)
for x in range(100):
    for y in range(100):
        for z in range(100):
            m = x**2 + y**2 + z**2 + x*y + y*z + z*x
            if 1 <= x * y * z and 0 <= m <= n:
                ans[m] += 1

for i in range(n):
    print(ans[i+1])