while True:
    n = int(input())
    if n == 0:
        break

    W = list(map(int, input().split()))

    dp = [[0] * n for _ in range(n)]

    for w in range(2, n+1):
        for i in range(n):
            j = i + w - 1
            if j >= n:
                continue

            if dp[i+1][j-1] == w-2 and abs(W[i] - W[j]) <= 1:
                dp[i][j] = w
            for k in range(i, j):
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k+1][j])

    print(dp[0][n-1])
