def main():
    S = input()
    n = len(S)

    for i in range(1 << n-1):
        t = ''
        for j in range(n-1):
            t += S[j]
            if i & (1 << j):
                t += '+'
            else:
                t += '-'
        t += S[n-1]
        if eval(t) == 7:
            print(t+'=7')
            break


if __name__ == '__main__':
    main()
