def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    
    divisors.sort()
    return divisors

n = int(input())

div = make_divisors(n)
ans = sum(div[:-1])

if ans < n:
    print("Deficient")
elif ans == n:
    print("Perfect")
else:
    print("Abundant")
