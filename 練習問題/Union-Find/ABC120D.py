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


n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

ans = [0] * m
ans[m-1] = n * (n-1) // 2
UF = UnionFind(n)
for i in range(m-1, 0, -1):
    a, b = ab[i]
    if UF.same(a-1, b-1):
        ans[i-1] = ans[i]
    else:
        ans[i-1] = ans[i] - UF.size[UF.find(a-1)] * UF.size[UF.find(b-1)]
        UF.unite(a-1, b-1)

for a in ans:
    print(a)
