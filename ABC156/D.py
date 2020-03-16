import math

def cmb(n,k):
    result = 1.0
    for i in range(1,k+1):
        result *= (n-i+1)/i
    return result

def main():
    n, a, b = map(int, input().split(' '))
    
    ans = pow(2,n) - cmb(n,a) - cmb(n,b) - 1

    print(int(ans%(pow(10,9)+7)))

if __name__ == '__main__':
    main()
