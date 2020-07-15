from collections import Counter

n = int(input())
a = [list(input()) for _ in range(n)]
if n == 1:
    print(a[0][0])
else:
    counter = []
    for i in range(n):
        cnt = Counter(a[i])
        counter.append(cnt)

    ans = []
    for i in range(n//2):
        flag = False
        for k, v in counter[i].items():
            if counter[n-i-1][k] != 0:
                ans.append(k)
                flag = True
                break
        if not flag:
            print(-1)
            exit()
    tail = reversed(ans)

    if n % 2 == 1:
        print(''.join(map(str, ans))+a[n//2][0]+''.join(map(str, tail)))
    else:
        print(''.join(map(str, ans))+''.join(map(str, tail)))
