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


N, Q = map(int, input().split())

UF = UnionFind(N)

for i in range(Q):
    com, x, y = map(int, input().split())

    if com == 0:
        UF.unite(x, y)
    if com == 1:
        print(int(UF.same(x, y)))
