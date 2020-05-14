def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def lcm(a, b):
    return a // gcd(a, b) * b

N, M = map(int, input().split())
A = list(map(int, input().split()))
A = [a//2 for a in A]

while A[0] % 2 == 0:
    for i in range(N):
        if A[i] % 2 != 0:
            print(0)
            exit()
        A[i] //= 2
    M //= 2

for i in range(N):
    if A[i] % 2 == 0:
        print(0)
        exit()

lcm_ = 1
for i in range(N):
    lcm_ = lcm(lcm_, A[i])
    if M < lcm_:
        print(0)
        exit()

print((M // lcm_ + 1) // 2)
