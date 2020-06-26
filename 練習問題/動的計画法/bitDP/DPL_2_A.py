V, E = map(int, input().split())

dis = [[float("inf")] * V for _ in range(V)]
for i in range(E):
	s, t, d = map(int, input().split())
	dis[s][t] = d

dp = [[-1] * V for _ in range(1<<V)]

def rec(s, v):
	if dp[s][v] >= 0:
		return dp[s][v]

	if s == (1<<V) -1 and v == 0:
		dp[s][v] = 0
		return 0
	
	res = float("inf")
	for u in range(V):
		if not s >> u&1:
			res = min(res, rec(s|(1<<u), u)+dis[v][u])
	
	dp[s][v] = res
	return res

res = rec(0, 0)
if res == float("inf"):
	print(-1)
else:
	print(res)
