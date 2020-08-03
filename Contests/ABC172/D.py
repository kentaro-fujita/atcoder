def num_divisors_table(n):
    table = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            table[j] += 1

    return table


n = int(input())
t = num_divisors_table(n)

ans = 0
for k in range(1, n+1):
    ans += k * t[k]
print(ans)
