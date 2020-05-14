# 頻出関数
## 整数問題
### 約数
```
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    
    # divisors.sort()
    return divisors
```
### 最大公約数
```
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
```
### 最小公倍数
```
def lcm(x, y):
    d = gcd(x, y)
    return a // x * y
```
### 素因数分解
```
def prime_factorize(n):
    res = []
    for i in range(2, int(n**(1/2))+1):
        if n % i != 0: continue
        num = 0
        while n % i == 0:
            num += 1
            n /= i
        res.append((i, num))
    if n != 1:
        res.append((n, 1))
    
    return res
```
### べき乗 (10**9+7で割った余り)
```
mod = 10**9 + 7

def pow(x, y):
    ret = 1
    while y:
        if y & 1:
            ret = ret * x % mod
        x = x * x % mod
        y >>= 1
    
    return ret
```
### 二項係数 (10**9+7で割った余り)
```
def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7 #出力の制限
N = 10**4
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

a = cmb(n,r,mod)
```
### 素数判定
```
def is_prime(n):
    if n == 1: return False

    for k in range(2, int(n**(1/2)) + 1):
        if n % k == 0:
            return False

    return True
```
### 素数列挙
```
def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]
```