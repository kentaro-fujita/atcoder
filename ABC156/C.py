def main():
    N = int(input())
    X = list(map(int, input().split(' ')))

    ans = []
    for p in range(100):
        dis = 0
        for x in X:
            dis += pow((x-p), 2)
        ans.append(dis)

    print(min(ans))

if __name__ == '__main__':
    main()


"""
A, B = map(int, input().split(' '))
N = list(map(int, input().split(' ')))
"""