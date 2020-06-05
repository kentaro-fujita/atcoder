a, b = map(int, input().split())

def solve(x):
    if x % 2 == 1:
        return (x+1) // 2 % 2
    else:
        return ((x+2) // 2 % 2) ^ (x+1)

print(solve(b) ^ solve(a-1))
