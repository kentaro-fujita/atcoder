def main():
    A = []
    A.append(list(map(int, input().split(' '))))
    A.append(list(map(int, input().split(' '))))
    A.append(list(map(int, input().split(' '))))

    N = int(input())
    b = []
    for i in range(N):
        b.append(int(input()))

    Af = []
    for i in range(3):
        for j in range(3):
            if A[i][j] in b:
                A[i][j] = 0
            Af.append(A[i][j])
    
    bingo_list = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    ans = False
    for bingo in bingo_list:
        _sum = 0
        for i in bingo:
            _sum += Af[i]
            if _sum == 0:
                ans = True
    
    if ans:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

"""
A, B = map(int, input().split(' '))
N = list(map(int, input().split(' ')))
"""