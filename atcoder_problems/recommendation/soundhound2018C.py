n, m, d = map(int, input().split())
k = (max(0, n - d) * 2 if d else n)
print(k * (m - 1) / n**2)
