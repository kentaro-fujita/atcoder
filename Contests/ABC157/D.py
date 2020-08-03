N, M, K = map(int, input().split())
F = [[] for _ in range(N)]
B = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    F[a-1].append(b-1)
    F[b-1].append(a-1)

for i in range(K):
    c, d = map(int, input().split())
    B[c-1].append(d-1)
    B[d-1].append(c-1)


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
        else:
            self.par[y] = x
            self.size[x] += self.size[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


UF = UnionFind(N)
for iam in range(N):
    for friend in F[iam]:
        UF.unite(iam, friend)

ans = [UF.size[UF.find(iam)] - 1 for iam in range(N)]
for iam in range(N):
    ans[iam] -= len(F[iam])

for iam in range(N):
    for block in B[iam]:
        if UF.find(iam) == UF.find(block):
            ans[iam] -= 1

print(*ans, sep=' ')
