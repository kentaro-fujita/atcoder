n, a, b = map(int, input().split())
s = [int(input()) for _ in range(n)]

na = sum(s) / n
nb = max(s) - min(s)

if nb == 0 and b != 0:
    print(-1)
    exit()

p = nb / b
q = a - na / p 

print(1/p, q)
