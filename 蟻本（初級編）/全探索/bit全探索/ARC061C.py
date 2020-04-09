def main():
    S = input()
    n = len(S)

    ans = 0
    for i in range(1<<n-1):
        t = ''
        for j in range(n):
            t += S[j]
            if i & (1 << j):
                t += '+'
        ans += eval(t)

    print(ans)

if __name__ == '__main__':
    main()