X, Y, A, B, C = map(int, input().split())
p = list(map(int, input().split()))
p.sort(reverse=True)
topP = p[:X]

q = list(map(int, input().split()))
q.sort(reverse=True)
topQ = q[:Y]

r = list(map(int, input().split()))
r.sort(reverse=True)

concat = topP + topQ + r
concat.sort(reverse=True)
top = concat[:X+Y]

print(sum(top))
