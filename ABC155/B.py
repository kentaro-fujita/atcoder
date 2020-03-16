def main():
    N = int(input())
    A = list(map(int, input().split(' ')))

    flag = True
    for i in range(N):
        if A[i] % 2 == 0:
            if A[i] % 3 == 0 or A[i] % 5 == 0:
                pass
            else:
                flag = False

    if flag:
        print("APPROVED")
    else:
        print("DENIED")


if __name__ == '__main__':
    main()

"""
A, B = input().split(' ')
A, B = map(int, input().split(' '))
N = list(map(int, input().split(' ')))
"""