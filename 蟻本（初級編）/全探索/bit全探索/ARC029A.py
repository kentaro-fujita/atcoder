def main():
    N = int(input())
    t = [int(input()) for _ in range(N)]

    ans = 4*50
    for i in range(1 << N):
        plate1 = 0
        plate2 = 0
        for j in range(N):
            if i & (i << j):
                plate1 += t[j]
            else:
                plate2 += t[j]
        ans = min(ans, max(plate1, plate2))

    print(ans)


if __name__ == '__main__':
    main()
