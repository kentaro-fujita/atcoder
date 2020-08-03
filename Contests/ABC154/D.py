def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))

    p = [(p_i+1)/2 for p_i in p]
    ans = 0
    for i in range(N-K+1):
        if i == 0:
            sum_ = sum(p[i:i+K])
        else:
            sum_ = sum_ + p[i+K-1] - p[i-1]
        ans = max(ans, sum_)

    print(ans)


if __name__ == '__main__':
    main()
