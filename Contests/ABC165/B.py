X = int(input())

ans = 100
i = 1
while True:
    ans = int(ans*1.01)
    if ans >= X:
        print(i)
        exit()
    else:
        i += 1
