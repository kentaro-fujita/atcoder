k = int(input())

if k % 2 == 0:
    print(-1)
    exit()

num = 0
for i in range(10**6+1):
    num += 7 * pow(10, i, k)
    if num % k == 0:
        print(i+1)
        exit()

print(-1)
