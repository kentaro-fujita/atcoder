S = input()
N = len(S)
P = 2019

mod = 0
count = [0] * P
ten = 1
count[mod] += 1
for i in range(N):
    mod = (mod + int(S[N-i-1]) * ten) % P
    ten = ten * 10 % P
    count[mod] += 1

res = 0
for c in count:
    res += (c * (c - 1)) // 2

print(res)
