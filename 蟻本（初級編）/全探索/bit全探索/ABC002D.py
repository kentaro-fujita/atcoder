import itertools

def main():
    N, M = map(int, input().split())
    friend = [[0] * N for _ in range(N)]
    for _ in range(M):
        x, y = map(int, input().split())
        friend[x-1][y-1] = 1
        friend[y-1][x-1] = 1

    ans = 0
    for i in range(1<<N):
        group = []
        for j in range(N):
            if i & (1<<j):
                group.append(j)
        
        flag = True
        for i in itertools.combinations(group, 2):
            if friend[i[0]][i[1]] == 0:
                flag = False
                break
        if flag:
            ans = max(ans, len(group))
    
    print(ans)

if __name__ == '__main__':
    main()