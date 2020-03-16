def main():
    N, M = map(int, input().split(' '))
    s = []
    c = []
    for i in range(M):
        si, ci = map(int, input().split(' '))
        s.append(si)
        c.append(ci)
    
    ans = [0]*N
    flag = False
    for i in range(M):
        if ans[s[i]-1] == 0:
            ans[s[i]-1] = c[i]
        elif ans[s[i]-1] == c[i]:
            ans[s[i]-1] = c[i]
        else:
            flag = True
    
    if flag:
        print("-1")
    elif ans[0] == 0 and N != 1:
        print("-1")
    else:
        for i in range(N):
            print(ans[i], end='')
        print('')

if __name__ == '__main__':
    main()

"""
A, B = map(int, input().split(' '))
N = list(map(int, input().split(' ')))
"""