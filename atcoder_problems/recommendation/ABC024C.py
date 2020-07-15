n, d, k = map(int, input().split())

lr = [list(map(int, input().split())) for _ in range(d)]
st = [list(map(int, input().split())) for _ in range(k)]

for s, t in st:
    for i, (l, r) in enumerate(lr):
        if s <= t:
            if l <= s <= r:
                s = r
                if t <= r:
                    print(i+1)
                    break
        else:
            if l <= s <= r:
                s = l
                if l <= t:
                    print(i+1)
                    break
