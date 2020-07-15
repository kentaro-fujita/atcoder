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


n, m, k = map(int, input().split())
edges = []
for i in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a-1, b-1))
edges.sort()

if k == n:
    print(0)
    exit()


def kruskal(n, edges):
    uf = UnionFind(n)
    trees = n
    res = 0
    for c, a, b in edges:
        if not uf.same(a, b):
            uf.unite(a, b)
            res += c
            trees -= 1
            if trees == k:
                return res
    return res


print(kruskal(n, edges))
