from collections import Counter

n = int(input())
a = list(map(int, input().split()))

cnt = Counter(a)

ans = []
sum_ = sum(a)
q = int(input())
for i in range(q):
    b, c = map(int, input().split())
    bv, cv = cnt[b], cnt[c]
    sum_ += c*(cv+bv) - b*bv - c*cv
    cnt[c] += bv
    cnt[b] = 0
    ans.append(sum_)

print("\n".join(map(str, ans)))
