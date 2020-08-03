def main():
    N, K = map(int, input().split())

    div = N // K
    min1 = abs(N - div*K)
    min2 = abs(N - (div+1)*K)

    print(min(min1, min2))


if __name__ == '__main__':
    main()
