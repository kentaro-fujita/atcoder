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

    def same(self, x, y):
        if self.find(x) == self.find(y):
            return True
        else:
            return False


N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]

ans = 0
for i in range(M):
    UF = UnionFind(N)

    for j in range(M):
        a, b = ab[j]
        if j != i:
            UF.unite(a-1, b-1)

    s = set()
    for j in range(N):
        s.add(UF.find(j))

    if len(s) > 1:
        ans += 1

print(ans)
