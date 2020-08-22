from bisect import bisect_right


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


n, k = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))

uf = UnionFind(n)  # n: 頂点数

for i in range(n):
    uf.union(i, p[i]-1)

ans = []
for root in uf.roots():
    l = [c[member] for member in uf.members(root)]
    l.sort()

    size = len(l)
    d = k // size
    m = k % size
    lb = bisect_right(l, 0)
    print(l, lb)
    print(d, m)
    print(sum(l) * d, sum(l[lb:m+1]), sum(l[lb:min(k, size)]))
    ans.append(sum(l) * d + sum(l[lb:m+1]))
    if l[lb:min(k, size)]:
        ans.append(sum(l[lb:min(k, size)]))
ans.append(max(c))

print(ans)
