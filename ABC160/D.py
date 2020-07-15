def main():
    N, X, Y = map(int, input().split())
    ans = [0] * (N - 1)

    dist = 0

    for i in range(1, N):
        for j in range(i + 1, N + 1):
            dist = min(j - i, abs(i - X) + abs(j - Y) + 1)
            ans[dist - 1] += 1

    for i in range(N - 1):
        print(ans[i])


if __name__ == '__main__':
    main()
