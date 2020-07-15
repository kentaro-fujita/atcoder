import numpy as np


def main():
    A = []
    for _ in range(3):
        A += list(map(int, input().split()))

    N = int(input())

    b = []
    for _ in range(N):
        b.append(int(input()))

    for v in b:
        if v in A:
            index = A.index(v)
            A[index] = 0

    bingo_list = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for bingo in bingo_list:
        if sum(np.array(A)[bingo]) == 0:
            print("Yes")
            exit()

    print("No")


if __name__ == '__main__':
    main()
