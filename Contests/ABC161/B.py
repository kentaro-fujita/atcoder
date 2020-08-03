def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    sumA = sum(A)

    ans = True
    for i in range(M):
        if (A[i] < sumA / (4*M)):
            ans = False

    if ans:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
