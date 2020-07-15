b = input().split()
n = int(input())
a = [input() for _ in range(n)]


def f(s):
    t = ""
    for i, c in enumerate(s):
        k = b.index(c)
        t += str(k)
    return int(t)


for ans in sorted(a, key=lambda x: f(x)):
    print(ans)
