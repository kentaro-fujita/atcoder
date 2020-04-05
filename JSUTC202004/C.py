def dfs(a: int, b: int, c: int) -> int:
    if a == b == c == 0:
        return 1

    result = 0
    if a > b:
        result += dfs(a - 1, b, c)
    if b > c:
        result += dfs(a, b - 1, c)
    if c:
        result += dfs(a, b, c - 1)

    return result

def main():
    a1, a2, a3 = list(map(int, input().split()))

    ans = dfs(a1, a2, a3)

    print(ans)

if __name__ == '__main__':
    main()