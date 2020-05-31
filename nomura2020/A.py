h1, m1, h2, m2, k = map(int, input().split())


if h2 >= h1:
    mins = (h2 - h1) * 60 + m2 - m1
    ans = mins - k

print(ans)
