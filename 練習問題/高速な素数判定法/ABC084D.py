def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return is_prime

is_prime = primes(10**5)
like = [0] * 10**5
for i in range(3, 10**5, 2):
    if is_prime[i] and is_prime[(i+1)//2]:
        like[i] = 1

cusum = [0] * 10**5
for i in range(3, 10**5, 2):
    cusum[i] = cusum[i-2] + like[i]

Q = int(input())
for i in range(Q):
    l, r = map(int, input().split())

    if l == 1:
        print(cusum[r])
    else:
        print(cusum[r] - cusum[l-2])
