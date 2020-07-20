n = int(input())
t = [int(input()) for _ in range(n)]

ans = float("inf")
for i in range(1 << n):
    machine1 = 0
    machine2 = 0
    for j in range(n):
        if i & 1 << j:
            machine1 += t[j]
        else:
            machine2 += t[j]
    ans = min(ans, max(machine1, machine2))

print(ans)
