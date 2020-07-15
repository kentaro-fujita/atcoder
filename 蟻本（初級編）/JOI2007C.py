import bisect


def main():
    N, M = map(int, input().split())
    P = [0] + [int(input()) for _ in range(N)]
    P.sort()

    L = [P[i]+P[j] for i in range(N+1)
         for j in range(i, N+1) if P[i]+P[j] <= M]
    L.sort()

    ans = 0
    for x in L:
        y = L[bisect.bisect_right(L, M-x) - 1]
        ans = max(ans, x+y)

    print(ans)


if __name__ == '__main__':
    main()
