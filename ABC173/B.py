n = int(input())
s = [input() for _ in range(n)]

cnt = {"AC": 0, "WA": 0, "TLE": 0, "RE": 0}
for v in s:
    cnt[v] += 1

for k, v in cnt.items():
    print(f"{k} x {v}")