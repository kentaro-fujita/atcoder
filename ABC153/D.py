H = int(input())

ans = 0
count = 0
while True:
    ans += 2**count
    if H == 1:
        break
    else:
        H //= 2
        count += 1

print(ans)