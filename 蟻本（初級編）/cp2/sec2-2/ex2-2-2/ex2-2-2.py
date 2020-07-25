n = int(input())
st = [list(map(int, input().split())) for _ in range(n)]

st.sort(key=lambda x: x[1])

ans = 0
t = 0
for i in range(n):
    if t < st[i][1]:
        ans += 1
        t = st[i][0]
print(ans)
