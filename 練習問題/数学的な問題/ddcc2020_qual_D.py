M = int(input())

s = 0
dig = 0
for i in range(M):
    d, c = map(int, input().split())
    s += d * c
    dig += c

print(dig - 1 + (s - 1) // 9)
