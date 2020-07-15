def main():
    N, A, B = map(int, input().split(' '))

    div = int(N / (A+B))
    sub = N - (A+B)*div

    ans = div*A
    if sub <= A:
        ans += sub
    else:
        ans += A

    print(ans)


if __name__ == '__main__':
    main()
