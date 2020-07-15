import heapq


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


V, E = map(int, input().split())
edges = []
for i in range(E):
    s, t, w = map(int, input().split())
    edges.append((w, s-1, t-1))
edges.sort()

# クラスカル法


def kruskal(n, edges):
    U = UnionFind(n)
    res = 0
    for e in edges:
        w, s, t = e
        if not U.same(s, t):
            res += w
            U.unite(s, t)
    return res


print(kruskal(V, edges))

##################################

V, E = map(int, input().split())

edges = [[] for _ in range(V)]
for _ in range(E):
    s, t, w = map(int, input().split())

    edges[s-1].append([w, t-1])
    edges[t-1].append([w, s-1])

# プリム法


def prim(n, w, edges):
    used = [True] * n  # True:不使用
    edgelist = []
    for e in edges[0]:
        heapq.heappush(edgelist, e)
    used[0] = False
    res = 0
    while len(edgelist) != 0:
        minedge = heapq.heappop(edgelist)
        if not used[minedge[1]]:
            continue
        v = minedge[1]
        used[v] = False
        for e in edges[v]:
            if used[e[1]]:
                heapq.heappush(edgelist, e)
        res += minedge[0]
    return res


print(prim(V, E, edges))
